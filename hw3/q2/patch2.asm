jmp $+0x95
mov dx, 0x2123
cmp dx, [eax]
jne $+0x60
add eax, 2
sub esp, 8
sub esp, 0xC
push eax
call $-0x185
add esp, 0xA
pop eax
jmp $+0x60
