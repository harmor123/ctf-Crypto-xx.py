# Time: 2023/4/21 1:47

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_char = ord(char) - shift
            if char.islower():
                if shifted_char < ord('a'):
                    shifted_char += 26
            elif char.isupper():
                if shifted_char < ord('A'):
                    shifted_char += 26
            plaintext += chr(shifted_char)
        else:
            plaintext += char
    return plaintext

def main():
    ciphertext = input("Enter the ciphertext: ")
    shift = int(input("Enter the shift value: "))
    plaintext = caesar_decrypt(ciphertext, shift)
    print("The decrypted text is:", plaintext)

if __name__ == "__main__":
    main()
