# Time: 2023/4/21 3:10


def rot47_decode(ciphertext: str) -> str:
    plaintext = ""
    for c in ciphertext:
        if 33 <= ord(c) <= 126:
            plaintext += chr((ord(c) - 33 - 47) % 94 + 33)
        else:
            plaintext += c
    return plaintext


def main():
    ciphertext = input('需要解密的内容是：')
    decrypted_text = rot47_decode(ciphertext)
    print('明文:', decrypted_text)


if __name__ == "__main__":
    main()
