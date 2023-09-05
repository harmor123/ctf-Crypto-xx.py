# -*- coding: utf-8 -*-
# Time: 2023/6/7 9:06
# Editor:harmor
import json

fp = open('stu2.json', 'r', encoding='utf8')

jsonst=json.load(fp)
print(jsonst)
lsst=jsonst['liststudent']
print(lsst)
for st in lsst:
    print(st['sid'])
    print(st['sname'])
    print(st['sex'])
    print(st['address'])
    print(st['class'])
    print('#'*100)