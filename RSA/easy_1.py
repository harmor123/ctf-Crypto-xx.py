# Time: 2023/4/20 19:26

"""
常用的库
import libnum  libnum.n2s(n) 数字转字符串 libnum.s2n(s)
gmpy2.mpz(n)初始化一个大整数
n=invert(m,phi)求mod phi的逆元
pow(m,e,n)求c^d mod n
gmpy2.is_prime(n) 素性检测
gmpy2.gcd(a,b)  欧几里得算法，最大公约数
gmpy2.gcdext(a,b)  扩展欧几里得算法
gmpy2.iroot(x,n) x开n次根
"""

import gmpy2

p = gmpy2.mpz(336771668019607304680919844592337860739)  # 初始化大整数 p （素数）
q = gmpy2.mpz(296173636181072725338746212384476813557)  # 初始化大整数 q （素数）
e = gmpy2.mpz(65537)
phi_n = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_n)  # e*d % phi_n == 1 求 d
print(d)
