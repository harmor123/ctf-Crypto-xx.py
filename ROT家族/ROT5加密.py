# Time: 2023/4/21 3:07
def rot5_encode(plaintext):
    ciphertext = ""
    for c in plaintext:
        if c.isdigit():
            new_digit = (int(c) + 5) % 10
            ciphertext += str(new_digit)
        else:
            ciphertext += c
    return ciphertext


def main():
    ciphertext = input('需要加密的内容是：')
    decrypted_text = rot5_encode(ciphertext)
    print('密文:', decrypted_text)


if __name__ == "__main__":
    main()
