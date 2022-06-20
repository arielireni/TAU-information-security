#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/user.h>

int pid = 0x12345678;

int main(int argc, char **argv) {
    // Make the malware stop waiting for our output by forking a child process:
    if (fork() != 0) {
        // Kill the parent process so we stop waiting from the malware
        return 0;
    } else {
        // Close the output stream so we stop waiting from the malware
        fclose(stdout);
    }

    // The rest of your code goes here
    struct user_regs_struct regs;
    int status;

    if (ptrace(PTRACE_ATTACH, pid, NULL, NULL) == -1) {
        perror("attach");
        return 1;
    }

    waitpid(pid, &status, 0);
    if (WIFEXITED(status)) { return 1; }

    // Do your magic here

    while(1) {
        ptrace(PTRACE_SYSCALL, pid, 0, 0);
        waitpid(pid, &status, 0);

        ptrace(PTRACE_GETREGS, pid, 0, &regs);
        
        long syscall = regs.orig_eax;
        if (syscall == 3) {
            regs.ebx = -1;
        }

        ptrace(PTRACE_SETREGS, pid, 0, &regs);
    
        ptrace(PTRACE_SYSCALL, pid, 0, 0);
        waitpid(pid, &status, 0);
        if (WIFEXITED(status)) { return 0; }
    }

    return 0;
}


