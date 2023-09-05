# Time: 2023/4/21 1:58
import math

def fence_decode(c:str, k:int):
    kn = int(len(c) / k)
    pt = ''
    yushu = len(c) % k
    steps = []
    if len(c) % k == 0:           #不存在余数
        step = kn
        for i in range(k):
            steps.append(step)
    else:                           #存在余数
        big_step = math.ceil(len(c) / k)
        small_step = int(len(c) / k)
        for p in range(yushu):
            steps.append(big_step)
        for q in range(k - yushu):
            steps.append(small_step)
    n_column = 0
    while n_column < math.ceil(len(c) / k):
        count_steps = 0
        for one_step in steps:
            if len(pt) == len(c):
                break
            else:
                pt += c[n_column + count_steps]
                count_steps += one_step
        n_column += 1
    return pt

def main():
    ciphertext = input("输入密文: ")
    key = int(input("输入key: "))
    r = fence_decode(ciphertext, key)
    print('Decrypted text:', r)

if __name__ == "__main__":
    main()