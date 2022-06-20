#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int pid = 0x12345678;
int address = 0x11112222;
int shellcode = 0x90c3c031; // xor eax, eax; ret in bytes

int main() {
    if (ptrace(PTRACE_ATTACH, pid, NULL, NULL) == -1) {
        perror("attach");
        return 1;
    }
    int status;
    waitpid(pid, &status, 0);
    if (WIFEXITED(status)) { return 1; }
    
    // Do your magic here

    if((ptrace(PTRACE_POKETEXT, pid, address, (void *)shellcode)) < 0) {
        perror("poketext");
        return 1;
    }


    if (ptrace(PTRACE_DETACH, pid, NULL, NULL) == -1) {
        perror("detach");
        return 1;
    }
    return 0;
}

