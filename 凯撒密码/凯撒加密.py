# Time: 2023/4/21 1:20

def kaisa_encode(c:str,k:int):
    result = ''
    for word in c:
        if word.isalpha():
            if word.isupper():
                tword = chr((ord(word)-ord('A') + k) % 26 + ord('A'))
            else:
                tword = chr((ord(word)-ord('a') + k) % 26 + ord('a'))
        else:
            tword = word
        result += tword
    return result

def main():
    c = input("输入明文: ")
    k = int(input("输入密钥: "))
    mw = kaisa_encode(c, k)
    print("密文: ", mw)

if __name__ == "__main__":
    main()


