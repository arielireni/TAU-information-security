# Declare the assembly flavor to use the intel syntax.
.intel_syntax noprefix

# Define a symbol to be exported from this file.
.global my_function

# Declare symbol type to be a function.
.type my_function, @function

# Code follows below.

# NOTE: I used external piece of code from here https://montcs.bloomu.edu/~bobmon/Code/Asm.and.C/Asm.Nasm/fibonacci.shtml

my_function:
    # 1. Read the input to the function from the stack.
    # 2. Save the result in the register EAX (and then return!).
    # 3. Make sure to include a recursive function call (the recursive fun    ction
    #  can be this function, or a helper function defined later in this     file).

    PUSH EBP
    MOV EBP, ESP
    SUB ESP, 16
    
    MOV EAX, [EBP + 8]
    CMP EAX, 0
    JL finish_invalid
    CMP EAX, 2
    JAE recursive_fib

    XOR EDX, EDX
    JMP finish

recursive_fib:
    SUB EAX, 2
    PUSH EAX
    
    # Compute fib(n-2)
    CALL my_function
    
    # Calculate fib(n-2)^2 and save this value
    IMUL EAX, EAX
    IMUL EDX, EDX
    MOV [EBP-8], EAX
    MOV [EBP-4], EDX

    MOV EAX, [EBP+8]
    SUB EAX, 1
    PUSH EAX
    
    # Compute fib(n-1)
    CALL my_function

    # Calculate fib(n-1)^2 and save this value
    IMUL EAX, EAX
    IMUL EDX, EDX
    MOV [EBP-16], EAX
    MOV [EBP-12], EDX

    # Calulate fib(n-1)^2 + fib(n-2)^2 and finish
    MOV EAX, [EBP-8]
    MOV EDX, [EBP-4]
    ADD EAX, [EBP-16]
    ADC EDX, [EBP-12]

finish:
    MOV ESP, EBP
    POP EBP
    RET

finish_invalid:
    MOV ESP, EBP
    POP EBP
    MOV EAX, -1
    RET
