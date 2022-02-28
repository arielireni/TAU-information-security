# Declare the assembly flavor to use the intel syntax.
.intel_syntax noprefix

# Define a symbol to be exported from this file.
.global my_function

# Declare symbol type to be a function.
.type my_function, @function

# Code follows below.

my_function:
    # This code reads the first argument from the stack into EBX.
    # (If you need, feel free to edit/remove this line).
    # Save the current value of EBX
    PUSH EBX
    MOV EBX, DWORD PTR [ESP + 8]

    # <<<< PUT YOUR CODE HERE >>>>
    
    # 1. Read the input to the function from EBX.
    
    CMP EBX, 1
    JL _RETURN_ZERO

    # Initialize loop counter and enter loop (from 1 to n-1)
    MOV ECX, 1
    _LOOP:
    MOV EDX, ECX
    IMUL EDX, EDX # Compute the squared current value
    CMP EDX, EBX # Check if the current value is the square root of the inpuf
    JE _RETURN_SQRT
    INC ECX
    CMP ECX, EBX
    JNE _LOOP

    # If the input is less than 1 or there isn't exact root
    _RETURN_ZERO:
    # Restore the value of EBX
    POP EBX
    MOV EAX, 0
    JMP _FINISH

    _RETURN_SQRT:
    # Restore the value of EBX
    POP EBX
    MOV EAX, ECX
    JMP _FINISH


    # 2. Save the result in the register EAX.

    # This returns from the function (call this after saving the result in EAX).
    # (If you need, feel free to edit/remove this line).
    _FINISH:

    RET
