# -*- coding: utf-8 -*-
# Time: 2023/7/18 0:00
# Editor:harmor
import gmpy2
from Crypto.Util.number import *
from gmpy2 import *

# 已知n、e、dp、c，求m
def decrypt(e,n,c,dp):
    for x in range(1, e):
        if(e*dp%x==1):
            p=(e*dp-1)//x+1
            if(n%p!=0):
                continue
            q=n//p
            phin=(p-1)*(q-1)
            d=gmpy2.invert(e, phin)
            m=gmpy2.powmod(c, d, n)
            if(len(hex(m)[2:])%2==1):
                continue
            print(bytes.fromhex(hex(m)[2:]))

#已知p、q、dp、dq、c，求m。

def decrypt(p,q,dp,dq,c):
    n = p*q
    phin = (p-1)*(q-1)
    dd = gmpy2.gcd(p-1, q-1)
    d=(dp-dq)//dd * gmpy2.invert((q-1)//dd, (p-1)//dd) * (q-1) +dq
    print(d)

    m = gmpy2.powmod(c, d, n)
    print(bytes.fromhex(hex(m)[2:]))