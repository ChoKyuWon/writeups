def hash(_rawarray):
    h = 3134132
    for i in range(len(_rawarray)):
        h = int.from_bytes(_rawarray[i], 'big') ^ h
        h *= 6745203
        l = len(hex(h))
        if l > 18:
            hex(h)[l - 16:]
            h = int(hex(h)[l - 16:], 16)
    return h

def flag(h):
    if len(hex(h)) < 18:
        h = '0' * (18 - len(hex(h))) + hex(h)[2:]
    else:
        h = hex(h)[2:]
    __rawarray = []
    for i in range(0, len(h), 2):
        __rawarray.append(h[i:i+2])
    
    adhoc = [-0x7d, +0x7c, 0, -0x51]
    for i, ad in enumerate(adhoc):
        tmp = int(__rawarray[7-i],16) + ad
        if tmp < 0:
            tmp += 0x100
        if tmp > 0x100:
            tmp -= 0x100
        __rawarray[7-i] = hex(tmp)[2:]

    target = __rawarray[4:][::-1]
    #print(target)
    if target == ['46', '6c', '61', '67'] or target == ['67', '61', '6c', '46']:
        print(target)
        return True
    return False

def maketestcase(rawarray):
    for i in range(0x34, 0x34+10):
        for j in range(0x34, 0x34+10):
            for k in range(0x34, 0x34+10):
                sum = hex(pow(i,3)+pow(j,3)+pow(k,3))
                if sum[-2:] == '62':
                    for l1 in range(0x4d, 0x4d+10):
                        for i1 in range(0x34, 0x34+10):
                            for j1 in range(0x34, 0x34+10):
                                for k1 in range(0x34, 0x34+10):
                                    sum1 = hex(pow(i1,3)+pow(j1,3)+pow(k1,3)+pow(l1,3))
                                    if sum1[-2:] == '6b':
                                        for i2 in range(0x4d, 0x4d+10):
                                            for j2 in range(0x4d, 0x4d+10):
                                                for k2 in range(0x4d, 0x4d+10):
                                                    for l2 in range(0x22, 0x22+10):
                                                        sum3 = hex(pow(i2,3)+pow(j2,3)+pow(k2,3)+pow(l2,3))
                                                        if sum3[-2:] == 'bf':
                                                            for x in range(0x4d, 0x57):
                                                                
                                                                rawarray[0x100a] = bytes([i])
                                                                rawarray[0x200a] = bytes([j])
                                                                rawarray[0x300a] = bytes([k])

                                                                rawarray[0x400a] = bytes([i1])
                                                                rawarray[0x500a] = bytes([j1])
                                                                rawarray[0x600a] = bytes([k1])
                                                                rawarray[0x700a] = bytes([l1])

                                                                rawarray[0x800a] = bytes([x])

                                                                rawarray[0x900a] = bytes([i2])
                                                                rawarray[0xa00a] = bytes([j2])
                                                                rawarray[0xb00a] = bytes([k2])
                                                                rawarray[0xc00a] = bytes([l2])
                                                                
                                                                if flag(hash(rawarray)) == True:
                                                                    rawarray = swap(rawarray)
                                                                    f = open('test','wb')
                                                                    f.write(b''.join(rawarray))

def swap(rawarray):
    new_array = []
    for i in range(14):
        new_array.append(rawarray[i*0x1000 : (i+1)*0x1000])
    new_array.append(rawarray[0xe000:])

    for i in range(0,14,2):
        try:
            if (int.from_bytes(new_array[i][0], 'big') + int.from_bytes(new_array[i + 1][0], 'big')) & 1 == 0:
                new_array[i], new_array[i+1] = new_array[i + 1], new_array[i]
        except:
            print(i, len(new_array))
            exit()
    _rawarray = []
    for r in new_array:
        _rawarray += r
    return _rawarray

def main():
    with open('data', 'rb') as f:
        raw = f.read()
    rawarray = []
    for i in range(0, len(raw)):
        rawarray.append(raw[i:i+1])

    rawarray = swap(rawarray)
    
    rawarray[0xa] = b'\x07'
    rawarray[0xd00a] = b'\x0c'
    rawarray[0xe00a] = b'\x8b'

    maketestcase(rawarray)

if __name__=='__main__':
    main()

