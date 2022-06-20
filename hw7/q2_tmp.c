#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int pid = 0x12345678;
int address = 0x11112222;
unsigned char *shellcode = "\xB8\x00\x00\x00\x00\xC3\x90\x90";

int main() {
    if (ptrace(PTRACE_ATTACH, pid, NULL, NULL) == -1) {
        perror("attach");
        return 1;
    }
    int status;
    waitpid(pid, &status, 0);
    if (WIFEXITED(status)) { return 1; }
    
    // Do your magic here
    int i;
    uint32_t  *s = (uint32_t *) shellcode;
    uint32_t *d = (uint32_t *) address;
    for(i = 0 ; i < 8; i+= 4, s++, d++) {
        if((ptrace(PTRACE_POKETEXT, pid, d, *s)) < 0) {
            perror("poketext");
            return 1;
        }
    }


    if (ptrace(PTRACE_DETACH, pid, NULL, NULL) == -1) {
        perror("detach");
        return 1;
    }
    return 0;
}
