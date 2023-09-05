# Time: 2023/4/21 3:07


def rot5_decode(ciphertext):
    plaintext = ""
    for c in ciphertext:
        if c.isdigit():
            new_digit = (int(c) - 5) % 10
            plaintext += str(new_digit)
        else:
            plaintext += c
    return plaintext


def main():
    ciphertext = input('需要解密的内容是：')
    decrypted_text = rot5_decode(ciphertext)
    print('明文:', decrypted_text)


if __name__ == "__main__":
    main()
