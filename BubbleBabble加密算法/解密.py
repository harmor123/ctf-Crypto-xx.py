# -*- coding: utf-8 -*-
# Time: 2023/6/8 20:44
# Editor:harmor
"""
这里是这种加密算法的解释（为了方便大家，加密算法我复制到文末），
链接传送：http://wiki.yak.net/589/Bubble_Babble_Encoding.txt

附上解题代码，楼主用的python3.7,另外bubblepy这个库需要导入一下，
网址附上https://pypi.python.org/pypi/bubblepy/

"""

from bubblepy import BubbleBabble

# 导入包bubblepy
str1 = 'xinik-samak-luvag-hutaf-fysil-notok-mepek-vanyh-zipef-hilok-detok-damif-cusol-fezyx'
# str是待解密字符
Str = BubbleBabble()
print(Str.decode(str))
