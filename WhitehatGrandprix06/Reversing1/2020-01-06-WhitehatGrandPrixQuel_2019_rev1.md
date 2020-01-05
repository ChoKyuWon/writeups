# rev1
Open the binary using IDA. It is 32bit executable.
```C++
int __cdecl main(int argc, const char **argv, const char **envp){
  v30 = fopen("data", "rb");
  v29 = operator new[](0x3Cu);
  for ( i = 0; i <= 14; ++i )
    *(_DWORD *)(4 * i + v29) = operator new[](0x1000u);
  for ( j = 0; j <= 14; ++j )
    v39 = fread(*(void **)(4 * j + v29), 1u, 0x1000u, v30);
  fclose(v30);
  for ( k = 0; k <= 6; ++k )
  {
    if ( !((**(_BYTE **)(8 * k + v29) + **(_BYTE **)(8 * k + 4 + v29)) & 1) )
      std::swap<unsigned char *>(8 * k + v29, v29 + 8 * k + 4);
  }
  if ( *(_BYTE *)(*(_DWORD *)v29 + 10) != 7 || *(_BYTE *)(*(_DWORD *)(v29 + 52) + 10) != 12 )
    return 1;
  for ( l = 1; l <= 6; ++l )
  {
    v28 = *(_BYTE *)(*(_DWORD *)(4 * l + v29) + 10) - 52;
    if ( v28 > 9u )
      return 1;
  }
  for ( m = 7; m <= 11; ++m )
  {
    v28 = *(_BYTE *)(*(_DWORD *)(4 * m + v29) + 10) - 77;
    if ( v28 > 9u )
      return 1;
  }
  if ( *(unsigned __int8 *)(*(_DWORD *)(v29 + 48) + 10) - 34 > 9 )
    return 1;
  v4 = pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 4) + 10), 3.0);
  v5 = pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 8) + 10), 3.0) + v4;
  v28 = (signed int)(pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 12) + 10), 3.0) + v5);
  if ( v28 != 98 )
    return 1;
  v6 = pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 16) + 10), 3.0);
  v7 = pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 20) + 10), 3.0) + v6;
  v8 = pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 24) + 10), 3.0) + v7;
  v28 = (signed int)(pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 28) + 10), 3.0) + v8);
  if ( v28 != 107 )
    return 1;
  v9 = pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 36) + 10), 3.0);
  v10 = pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 40) + 10), 3.0) + v9;
  v11 = pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 44) + 10), 3.0) + v10;
  v28 = (signed int)(pow((long double)*(unsigned __int8 *)(*(_DWORD *)(v29 + 48) + 10), 3.0) + v11);
  if ( v28 != -65 )
    return 1;
  v27 = (unsigned __int8 *)operator new[](0xF000u);
  for ( n = 0; (signed int)(v39 + 57344) > n; ++n )
    v27[n] = *(_BYTE *)(*(_DWORD *)(4 * (n / 4096) + v29) + n % 4096);
  LODWORD(v12) = SHF(v27, v39 + 57344);
  flag(v12);
  v13 = 0;
  v14 = 27;
  v15 = -70;
  v16 = 48;
  v17 = 80;
  v18 = -79;
  v19 = 126;
  v20 = -44;
  v21 = 15;
  v22 = 68;
  v23 = 49;
  v24 = 119;
  v25 = -42;
  v26 = -75;
  for ( ii = 0; ii <= 13; ++ii )
    *(_BYTE *)(*(_DWORD *)(4 * ii + v29) + 10) = *(&v13 + ii);
  v30 = fopen("output.png", "wb");
  for ( jj = 0; jj <= 13; ++jj )
    fwrite(*(const void **)(4 * jj + v29), 1u, 0x1000u, v30);
  fwrite(*(const void **)(v29 + 56), 1u, v39, v30);
  fclose(v30);
  std::operator<<<std::char_traits<char>>((std::ostream::sentry *)&std::cout, "\n");
  system("pause");
  return 0;
}
```
This is _main function's whole code. Let's break it down.
```C++
v30 = fopen("data", "rb");
v29 = operator new[](0x3Cu);
for ( i = 0; i <= 14; ++i )
  *(_DWORD *)(4 * i + v29) = operator new[](0x1000u);
for ( j = 0; j <= 14; ++j )
  v39 = fread(*(void **)(4 * j + v29), 1u, 0x1000u, v30);
fclose(v30);
```
Hmm... Type is unclear buy roughly guess that allocate ```v29```, array of ```int[15][0x1000]``` and put some chunck of data that read on ```data``` file. Let's call it ```rawarray```.
```C++
for ( k = 0; k <= 6; ++k )
{
  if ( !((**(_BYTE **)(8 * k + v29) + **(_BYTE **)(8 * k + 4 + v29)) & 1) )
    std::swap<unsigned char *>(8 * k + v29, v29 + 8 * k + 4);
}
```
If ```rawdata[2k][0] + rawdata[2k+1][0]``` is even, swap each. If that is odd, nothing happen. It is easy to understand, but hard to implement decoder.
```C++
if ( rawdata[0][10]) != 7 || rawdata[13][10] != 12 )
  return 1;
for ( l = 1; l <= 6; ++l )
{
  v28 = rawdata[l][10] - 52;
  if ( v28 > 9u )
    return 1;
}
for ( m = 7; m <= 11; ++m )
{
  v28 = rawdata[m][10] - 77;
  if ( v28 > 9u )
    return 1;
}
if ( rawdata[12][10] - 34 > 9 )
  return 1;
```
There are many condition checks. They refernece ```rawdata[n][10]```, and if it dosen't satisfiy condition, exit program. 
Pay attention to the sign, put the numbers on rawdata.
```C++
if((pow(rawdata[1][10], 3.0) + pow(rawdata[2][10], 3.0) + pow(rawdata[3][10], 3.0)) != 98)
    return 1;
if((pow(rawdata[4][10], 3.0) + pow(rawdata[5][10], 3.0) + pow(rawdata[6][10], 3.0) + pow(rawdata[7][10], 3.0)) != 98)
    return 1;
if((pow(rawdata[9][10], 3.0) + pow(rawdata[10][10], 3.0) + pow(rawdata[11][10], 3.0) + pow(rawdata[12][10], 3.0)) != 98)
    return 1;
```
This add ```rawdata[n][10]^3```, and use last byte to compare. Also pay attention on byte, just calculate this. It's hard to calcuate by hand, I use python script. 
```C++
v27 = (unsigned __int8 *)operator new[](0xF000u);
for ( n = 0; (signed int)(v39 + 57344) > n; ++n )
  v27[n] = *(_BYTE *)(*(_DWORD *)(4 * (n / 4096) + v29) + n % 4096);
LODWORD(v12) = SHF(v27, v39 + 57344);
flag(v12);
```
Now condition is end! This code allocate some array and combine ```rawarray[n]``` to one, and put it on ```SFH()``` and put SFH's return value on ```flag()```.
Hmm... SFH... It must mean ```Secure Hash Function```, isn't it? Let's analyse SFH.
```C++
signed __int64 __cdecl SHF(unsigned __int8 *a1, int a2)
{
  v4 = 3134132LL;
  for ( i = 0; i < a2; ++i )
  {
    LODWORD(v4) = a1[i] ^ (unsigned int)v4;
    v4 *= 6745203LL;
  }
  return v4;
}
```
It's simple! There is no effort for understanding.

```assembly
lea     eax, [ebp+var_30]
mov     [ebp+var_C], eax
mov     eax, [ebp+var_C]
movzx   eax, byte ptr [eax]
sub     eax, 7Dh
mov     [ebp+var_22], al
mov     eax, [ebp+var_C]
add     eax, 1
movzx   eax, byte ptr [eax]
add     eax, 7Ch
mov     [ebp+var_21], al
mov     eax, [ebp+var_C]
movzx   eax, byte ptr [eax+2]
mov     byte ptr [ebp+var_20], al
mov     eax, [ebp+var_C]
add     eax, 3
movzx   eax, byte ptr [eax]
sub     eax, 51h
mov     byte ptr [ebp+var_20+1], al
mov     [ebp+var_1E], 0
```
In flag function, I had a very hard time because IDA could not decompile it properly, but I don't know it and analyze only IDA decompilation. In assembly, get low 4byte of hashvalue and add some value on lowbyte, then ```strcmp``` with ```'Flag'```.
```C++
v13 = 0;
v14 = 27;
v15 = -70;
v16 = 48;
v17 = 80;
v18 = -79;
v19 = 126;
v20 = -44;
v21 = 15;
v22 = 68;
v23 = 49;
v24 = 119;
v25 = -42;
v26 = -75;
for ( ii = 0; ii <= 13; ++ii )
  *(_BYTE *)(*(_DWORD *)(4 * ii + v29) + 10) = *(&v13 + ii);
v30 = fopen("output.png", "wb");
for ( jj = 0; jj <= 13; ++jj )
  fwrite(*(const void **)(4 * jj + v29), 1u, 0x1000u, v30);
fwrite(*(const void **)(v29 + 56), 1u, v39, v30);
fclose(v30);
std::operator<<<std::char_traits<char>>((std::ostream::sentry *)&std::cout, "\n");
system("pause");
return 0;
```
And rest part of _main. C++ is hard to understand, but via dynamic analyse, this code overwrite ```rawarray[n][10]``` and save the ```rawarray``` on ```output.png```. ```output.png``` is provided so we just brute force some probability on ```rawarray[n][10]```. So I made python script to brute-force, and get flag finally!
Flag: ```WhiteHat{SHA1(8333769562446613979)}```
And you can see my python script on [here.](https://github.com/ChoKyuWon)