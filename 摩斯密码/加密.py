# Time: 2023/4/21 2:41


# 表示摩斯密码图的字典
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# 根据摩斯密码图对字符串进行加密的函数
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # 查字典并添加对应的摩斯密码
            # 用空格分隔不同字符的摩斯密码
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1个空格表示不同的字符
            # 2表示不同的词
            cipher += ' '

    return cipher

def main():
    message = input("需要加密的内容：")
    result = encrypt(message.upper())
    print (result)