# Time: 2023/4/25 19:30

'''
题目：变异的凯撒
附件：
加密密文：afZ_r9VYfScOeO_UL^RWUc
格式：flag{ }
'''
'''
凯撒密码本质是移位密码，需要写出字母的ASCII码表，观察变化；本题是afZ_r -> flag{ 观察移位  分别是是移 5、6、7、8、9位，以此类推
'''
str = 'afZ_r9VYfScOeO_UL^RWUc'
k = 5
for i in str:
    print(chr(ord(i)+k),end='')  #ord()函数是用于字符转成ASCII码，chr()则是相反
    k += 1
