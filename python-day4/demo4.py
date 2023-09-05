# -*- coding: utf-8 -*-
# Time: 2023/6/7 9:30
# Editor:harmor
"""
读取json文件并写入
"""
import json

fp = open('stu2.json', 'r', encoding='utf8')

jsonst = json.load(fp)
print(jsonst)
lsst = jsonst['liststudent']
print(lsst)
for st in lsst:
    print(st['sid'])
    print(st['sname'])
    print(st['sex'])
    print(st['address'])
    print(st['class'])
    print('#' * 100)
fp.close()

fp = open('stu2.json', 'w', encoding='utf8')

mydict = {"sid": 6, "sname": "长江", "sex": "男", "address": "长安", "class": "class1"}
lsst.append(mydict)
jsonst['liststudent'] = lsst

json.dump(jsonst, fp, ensure_ascii=False)
fp.close()
