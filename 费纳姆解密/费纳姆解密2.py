# Time: 2023/4/16 11:16

# coding: utf-8
## Fenham
## _Bonjour_Python3
#
Check_List_2num = {'A':'1000001','B':'1000010',
                   'C':'1000011','D':'1000100',
                   'E':'1000101','F':'1000110',
                   'G':'1000111','H':'1001000',
                   'I':'1001001','J':'1001010',
                   'K':'1001011','L':'1001100',
                   'M':'1001101','N':'1001110',
                   'O':'1001111','P':'1010000',
                   'Q':'1010001','R':'1010010',
                   'S':'1010011','T':'1010100',
                   'U':'1010101','V':'1010110',
                   'W':'1010111','X':'1011000',
                   'Y':'1011001','Z':'1011010'}

## key value对调
Check_List_2char = {value:key for key,value in     Check_List_2num.items()}

## 转换
def change2num(text):
    finish = []
    for i in text:
        finish.append(Check_List_2num[i])
    return finish

## 分组处理字符
def change2list(text):
    num = 0
    str = []
    while True:
        str.append(text[num:num+7])
        num += 7
        if(num > len(text) - 7):
            break
    return str

## XOR运算
def XOR(text,key):
    finish = ''
    for i in range(0,len(text)):
        if text[i] == key[i]:
            finish += '0'
        else:
            finish += '1'
    return finish

## 加解密

# 读文本文件
input = open('cipher.txt')
try:
    text = input.read()
finally:
    input.close()

file = open('key.txt')
try:
    key = file.read()
finally:
    file.close()

##转换key
key = change2num(key)
key = ''.join(key)

## 运算
finish = XOR(text,key)

## 转换字母
finish = change2list(finish)
str = ''
for i in finish:
    str += Check_List_2char[i]
print(str)