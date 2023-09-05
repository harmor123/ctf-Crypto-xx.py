# Time: 2023/4/21 1:58
import math

def fence_encode(p:str,k:int):
    c = ''     #初始化密文
    n = 0               #提取第n列字符
    while n < k:
        m = 0           #第m分组
        while m < len(p) / k:  #明文长度/加密密钥  即得分组个数
            if (m * k+ n) < len(p):
                c = c + p[int(m * k+ n)]
                m += 1
            else :
                break
        n += 1
    return c


def main():
    ciphertext = input("输入明文: ")
    key = int(input("输入key: "))
    r = fence_encode(ciphertext, key)
    print('密文:', r)

if __name__ == "__main__":
    main()