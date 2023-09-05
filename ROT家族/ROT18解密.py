# Time: 2023/4/21 2:16

def rot18_decode(text: str):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 18) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 18) % 26 + ord('A'))
        else:
            result += char
    return result

def main():
    ciphertext = input('需要解密的内容是：')
    decrypted_text = rot18_decode(ciphertext)
    print('明文:', decrypted_text)

if __name__ == "__main__":
    main()
