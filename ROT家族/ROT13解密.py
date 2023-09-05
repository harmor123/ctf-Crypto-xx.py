# Time: 2023/4/21 2:16

def rot13_decode(text: str):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

def main():
    ciphertext = input('密文是：')
    decrypted_text = rot13_decode(ciphertext)
    print('明文:', decrypted_text)

if __name__ == "__main__":
    main()
