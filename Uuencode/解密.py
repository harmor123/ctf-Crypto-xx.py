# Time: 2023/4/21 2:35

import uu

def uu_decode(encoded_string):
    input_data = encoded_string.encode()
    output_data = uu.decode(input_data)
    return output_data.decode()

def main():
    encoded_string = input('请输入密文字符串: ')
    decoded_string = uu_decode(encoded_string)
    print('明文字符串:', decoded_string)

if __name__ == '__main__':
    main()