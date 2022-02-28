# Declare the assembly flavor to use the intel syntax.
.intel_syntax noprefix

# Define a symbol to be exported from this file.
.global my_function

# Declare symbol type to be a function.
.type my_function, @function

# Code follows below.

my_function:

    # 1. Read the input to the function from the stack.
    MOV ECX, DWORD PTR [ESP + 4]
    # Check if the input < 0
    CMP ECX, 0
    JL _FINISH_INVALID

    # Store the current value of EBX
    PUSH EBX
    CMP ECX, 1
    JLE _FINISH_BASIC # if n = 0,1
    MOV EAX, 1 # otherwise, compute squarebonacci(n)
    MOV EBX, 0
    
    _LOOP:
    MOV EDX, EAX # save a(n-1)
    IMUL EBX, EBX 
    IMUL EAX, EAX
    ADD EAX, EBX # a(n)
    MOV EBX, EDX # new a(n-2) = old a(n-1)

    # preform this loop n-1 times (since we know a(0),a(1))
    DEC ECX
    CMP ECX, 2
    JGE _LOOP

    # 2. Save the result in the register EAX (and then return!).
    _FINISH:
    # Restore EBX
    POP EBX
    # the return value is already stored in EAX
    RET

    _FINISH_BASIC:
    # Restore EBX
    POP EBX
    MOV EAX, ECX
    RET

    _FINISH_INVALID:
    MOV EAX, -1
    RET

