# Move or Not
use IDA to decompile it.  
```c
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  int v4; // [rsp+8h] [rbp-38h]
  int i; // [rsp+Ch] [rbp-34h]
  char s2; // [rsp+10h] [rbp-30h]
  unsigned __int64 v7; // [rsp+38h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  i = 0;
  printf("First give me your password: ", a2, a3);
  __isoc99_scanf("%d", &v4);
  if ( v4 != 98416 )
  {
    puts("You don't know static analysis !");
    exit(0);
  }
  printf("Second give me your key: ");
  __isoc99_scanf("%d", &v4);
  v4 -= 49;
  for ( i = 0; i <= 11; ++i )
    *((_BYTE *)unknown_function + i) += v4;
  unknown_function(s1);
  printf("Then Verify your flag: ");
  __isoc99_scanf("%s", &s2);
  if ( !strcmp(s1, &s2) )
    puts("You are right. Congratulations !!");
  else
    puts("You don't know dynamic analysis !");
  return 0LL;
}
```
So easily find first key is hardcoded value, ```98416```. But Second key is seem more complex. It input some value on v4, and add it to ```unknown_function```'s first 11byte. Second key must 1byte, 0x00 to 0xFF, but don't know exact value. Via some test, I know the second key is '1', 50. If I can set breakpoint on strcmp, I can see what is s1 directly, but I can't.(It may because of ASLR, but don't know exact reason). So I reverse it only static analyse.  
```
objdump -s -j .data ./pro
```
To see data section in binary, I use this command and see ```unknown_function``` is folloing value:
```
7f2e264782c6007f061f4782c701802f0b4883c70180070d4883c7018007414883c701802f0d4883c7018007204883c70180073c4883c7018007484883c70180076f4883c70180073b4883c7018007594883c7018007464883c701802f144883c7018007084883c7018007014883c7018007314883c7018007184883c701802f094883c7018007114883c701802f054883c701802f454883c70180071a4883c70180072d4883c701802f0b4883c7018007554883c7018007184883c7018007194883c701802f3b4883c701802f094883c7018007084883c701800758c3
```
and to make analyse easier, I want to make original asm, and make following code.
```python
with open('pro.txt', 'r') as f:
    asm1 = f.readline() # first 11 byte of unknown_function
    asm2 = f.readline() # and rest parts of unknown_function

asm1arry = []
for i in range(0, len(asm1) - 2, 2):
    asm1arry.append(asm1[i:i+2])

newasma = ""
for asm in asmarry:
    n = format(int(asm, 16) + 1, 'x')
    if len(n) < 2:
        n = '0' + n
    newasmarray += n
newasm += asm2
print(newasm)
```
And I use [online assembler](https://defuse.ca/online-x86-assembler.htm). (After CTF, I realize modify binary and open it via IDA is perfect way, but during CTF, I use online assembler and analyze assembler.) Via assembly, I see ```unknown_function``` is used to encrypt flag by add or subtract some value on each flag byte. So I collect encrypted flag(s1) and key. Make python script to collect key is very graceful way, but key length is only 32byte so I just make key by my hand.
```python
s1 = '69417855 2e7c2633 300c2920 2848656832473a62 64795246 3b0a4f59 6e3d6c25'.replace(' ', '')
enc_flag = []
for i in range(0, len(s1), 2):
    enc_flag.append(s1[i:i+2])

key = [-0x27,0x20,-0xb,0xd, 0x41,-0xd, 0x20, 0x3c, 0x48, 0x6f, 0x3b, 0x59, 0x46, -0x14, 0x8, 0x1, 0x31, 0x18, -0x9, 0x11, -0x5, -0x45, 0x1a, 0x2d, -0xb, 0x55, 0x18,0x19, -0x3b, -0x9, 0x8, 0x58]
flag = ""
for i in range(32):
    flag += chr(int(enc_flag[i],16) + key[i])
print(flag)
```
So this is decrypt function, and flag is: ```BambooFox{dyn4mic_1s_4ls0_gr34t}```.