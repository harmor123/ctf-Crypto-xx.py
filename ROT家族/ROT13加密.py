# Time: 2023/4/21 2:24

def rot13_encode(text: str) -> str:
    ciphertext = ""
    for c in text:
        if c.isalpha():
            if c.isupper():
                new_ascii = (ord(c) - 65 + 13) % 26 + 65
            else:
                new_ascii = (ord(c) - 97 + 13) % 26 + 97
            ciphertext += chr(new_ascii)
        else:
            ciphertext += c
    return ciphertext


def main():
    ciphertext = input('明文：')
    decrypted_text = rot13_encode(ciphertext)
    print('密文:', decrypted_text)

if __name__ == "__main__":
    main()