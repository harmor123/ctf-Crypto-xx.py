# Time: 2023/4/21 2:50
import base64


def base64_encode(s: str):
    s = s.encode('utf-8')
    return base64.b64encode(s)
    return s


def main():
    message = input("需要加密的内容：")
    result = base64_encode(message)
    print(result)


# 执行主函数
if __name__ == '__main__':
    main()
