# 读取1.txt文件内容
with open('1.txt', 'r') as file:
    content = file.read()

# 将内容逆序
reversed_content = content[::-1]

# 将逆序后的内容写入2.txt文件
with open('2.txt', 'w') as file:
    file.write(reversed_content)
