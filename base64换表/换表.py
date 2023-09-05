# -*- coding: utf-8 -*-
# Time: 2023/6/7 1:39
# Editor:harmor
import base64
import string

string = "FlZNfnF6Qol6e9w17WwQQoGYBQCgIkGTa9w3IQKw"

tableBase64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
tableNew64  = "JKLMNOxyUVzABCDEFGH789PQIabcdefghijklmWXYZ0123456RSTnopqrstuvw+/"

'''
maketrans()：用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标；
translate()：法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中；
decode()：以encoding指定的编码格式解码字符串。
'''

'1.换表'
maketrans = str.maketrans(tableNew64, tableBase64)
'2.使用新表转换字符串'
translate = string.translate(maketrans)
'2.Base64解码'
flag = base64.b64decode(translate)

'''
三合一操作：
flag = base64.b64decode(string.translate(str.maketrans(tableNew, tableBase64)))
'''

print (flag)
