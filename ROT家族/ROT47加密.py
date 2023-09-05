# Time: 2023/4/21 3:10
def rot47_encode(plaintext: str) -> str:
    ciphertext = ""
    for c in plaintext:
        if 33 <= ord(c) <= 126:
            ciphertext += chr((ord(c) - 33 + 47) % 94 + 33)
        else:
            ciphertext += c
    return ciphertext


def main():
    ciphertext = input('需要加密的内容是：')
    decrypted_text = rot47_encode(ciphertext)
    print('明文:', decrypted_text)


if __name__ == "__main__":
    main()
