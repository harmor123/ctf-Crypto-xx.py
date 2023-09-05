# 让用户输入密文和密钥
cipher = input("请输入密文：")
key = input("请输入密钥：")
# 定义一个空字符串miyao，用于存储密钥的二进制表示
miyao = ""
# 将密钥的每个字符转换为二进制，并将它们拼接起来
for i in key:
    miyao += (str(bin(ord(i)))[2:])
# 定义一个空字符串flag1，用于存储解密后的二进制字符串
flag1 = ""
# 将密文和密钥进行异或运算，得到解密后的二进制字符串
for i in range(len(cipher)):
    flag1 += str(int(cipher[i])^int(miyao[i]))
# 将flag1按照7个一组进行分割
step = 7
b = [flag1[i:i+step] for i in range(0,len(flag1),step)]
flag = []
for i in b:
    flag.append(i)
# 定义一个空字符串final，用于存储最终的解密结果
final = ""
# 将每个7位二进制字符串转换为对应的ASCII字符，并将它们拼接起来
for i in flag:
    final += chr(int(i,2))
# 输出解密结果
print("flag为："+final)

#这段代码实现了费纳姆密码的解密。
# 首先让用户输入密文和密钥，然后将密钥的每个字符转换为二进制，并将它们拼接起来。
# 接着将密文和密钥进行异或运算，得到解密后的二进制字符串。
# 然后将解密后的二进制字符串按照7个一组进行分割，并将每个7位二进制字符串转换为对应的ASCII字符。最后输出解密结果。