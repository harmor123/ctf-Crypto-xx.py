# Time: 2023/5/21 11:37

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factorization(num):
    for i in range(2, num):
        if num % i == 0 and is_prime(i) and is_prime(num // i):
            return i, num // i
    return None

number = int(input("请输入一个32位以下的整数: "))
factors = prime_factorization(number)

if factors:
    print("两个素因子为:", factors)
else:
    print("无法找到两个素因子。")

