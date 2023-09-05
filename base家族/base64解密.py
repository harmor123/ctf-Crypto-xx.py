# Time: 2023/4/21 2:50

import base64


def base64_decode(s: str):
    s = base64.b64decode(s)
    return s


def main():
    message = input("需要解密的内容：")
    result = base64_decode(message)
    print(result)


# 执行主函数
if __name__ == '__main__':
    main()
