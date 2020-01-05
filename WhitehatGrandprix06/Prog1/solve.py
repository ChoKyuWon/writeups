from pwn import *

def gen(n):
    res = 13
    plus = 9
    _plus = 3

    for i in range(7,n):
        res = res + plus
        plus = plus + _plus
        if i % 2 == 1:
            _plus += 1
    return res

p = remote("15.164.75.32", 1999)

tmp = p.recv()
tmp = p.recv()
ans = gen(int(tmp.split('\n')[-2].split('=')[1]))
p.sendline(str(ans))
tmp = p.recv()
tmp = p.recv()
ans = gen(int(tmp.split('\n')[0].split('=')[1]))
p.sendline(str(ans))
tmp = p.recv()
tmp = p.recv()
ans = gen(int(tmp.split('\n')[0].split('=')[1]))
p.sendline(str(ans))
tmp = p.recv()
print(tmp)