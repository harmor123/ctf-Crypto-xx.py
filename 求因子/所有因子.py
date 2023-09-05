# Time: 2023/5/21 11:44
def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

number = int(input("请输入一个32位以下的整数: "))
factors = find_factors(number)

print("所有因子为:", factors)

