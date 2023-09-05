# -*- coding: utf-8 -*-
# Time: 2023/6/7 9:14
# Editor:harmor
import json

fp = open('stu3.json', 'a', encoding='utf-8')

dict={"sid": 1, "sname": "李白", "sex": "男", "address": "长安", "class": "class1"}
'''
复杂json文件写入
dict = {
    'liststudent':[
        {"sid": 1, "sname": "李白", "sex": "男", "address": "长安", "class": "class1"},
        {"sid": 2, "sname": "李白", "sex": "男", "address": "长安", "class": "class1"},
        {"sid": 3, "sname": "李白", "sex": "男", "address": "长安", "class": "class1"},
        {"sid": 4, "sname": "李白", "sex": "男", "address": "长安", "class": "class1"},
        {"sid": 4, "sname": "李白", "sex": "男", "address": "长安", "class": "class1"}
        ]
    }
'''
json.dump(dict, fp, ensure_ascii=False)
print('写入成功!')
fp.close()
