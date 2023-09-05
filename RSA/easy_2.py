# Time: 2023/4/20 19:34
"""
已知一段RSA加密的信息为：0xdc2eeeb2782c且已知加密所用的公钥：(n=322831561921859 e = 23)
请解密出明文，提交时请将数字转化为ascii码提交
比如你解出的明文是0x6162，那么请提交字符串ab
提交格式:PCTF{明文字符串}
"""
'''
http://factordb.com 大素数分解
'''
#https://www.freebuf.com/articles/web/287854.html 学习

# !/usr/bin/python
# coding:utf-8
import libnum
from Crypto.Util.number import long_to_bytes

c = 0xdc2eeeb2782c
n = 322831561921859
e = 23
q = 13574881
p = 23781539
d = libnum.invmod(e, (p - 1) * (q - 1))
m = pow(c, d, n)
print("m的值为:")
print(long_to_bytes(m))
