'''
题目：
import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)  #加密算法：仿射加密
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
'''

# y = (a*x+b)mod k
import gmpy2

d = gmpy2.invert(123, 256)  #求a在k的逆


def de(msg):#加密后的文件
    pt = []
    for char in msg:
        char = char - 18 #减去b
        char = d * char % 256
        pt.append(char)
    return bytes(pt)


with open('msg.txt') as f:
    ct = bytes.fromhex(f.read())

pt = de(ct)
print(pt.decode())
