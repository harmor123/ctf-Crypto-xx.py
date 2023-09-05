# -*- coding: utf-8 -*-
# Time: 2023/6/7 9:48
# Editor:harmor
import json
import sys
import os

'''
读取json文件并返回字典列表
'''


def readfiletolist():
    fp = open('stor.json', 'r', encoding='utf-8')
    if fp == None:
        print('文件没有内容！')
        return
    else:
        listproduct = json.load(fp)
        return listproduct

    fp.close()

    return None


'''
向json文件写入文件
'''


def writelisttofile(productlist: list):
    fp = open('stor.json', 'w', encoding='utf-8')
    json.dump(productlist, fp, ensure_ascii=False)
    print('写入文件成功！')
    fp.flush()
    fp.close()


'''
新增商品信息的函数
'''


def addproduct():
    # 从文件中获取文件信息
    productlist = readfiletolist()

    if productlist == None:
        productlist = []

    # 创建商品字典对象
    product = {}

    # 从键盘输入字典数据
    product['pid'] = input('输入商品编号:')
    product['pname'] = input('输入商品名称:')
    product['price'] = input('输入商品价格:')
    product['num'] = input('输入商品数量:')
    product['account'] = float(product['price']) * int(product['num'])
    productlist.append(product)  # 添加商品到商品集合

    # 写入集合到文件
    writelisttofile(productlist)
    print('保存成功！')


def showproductlist():
    # 从文件中获取文件信息
    productlist = readfiletolist()
    # print(productlist)

    if productlist == None or len(productlist) == 0:
        print('没有任何商品信息存在！')
        return
    # 输出商品信息
    print('====' * 5, '商品库存信息', '====' * 5)
    print('编号\t\t 商品名\t\t 价格\t\t 数量\t\t 小计\t\t')
    print('=' * 80)
    for pd in productlist:
        print('%s\t\t %s\t\t %s\t\t %s\t\t %s' % (pd['pid'], pd['pname'], pd['price'], pd['num'], pd['account']))

    pass


'''

'''


def findbyname():
    # 从文件中获取文件信息
    productlist = readfiletolist()
    # print(productlist)

    if productlist == None or len(productlist) == 0:
        print('没有任何商品信息存在！')
        return

    pname = input('输入要查询的商品名称:')
    pindex = -1  # 找到商品字典对象在列表集合中的索引位置
    i = 0
    for pd in productlist:
        if pd['pname'] == pname:
            print('找到的商品信息如下:')
            print('编号\t\t 商品名\t\t 价格\t\t 数量\t\t 小计\t\t')
            print('=' * 80)
            print('%s\t\t %s\t\t %s\t\t %s\t\t %s' % (pd['pid'], pd['pname'], pd['price'], pd['num'], pd['account']))
            pindex = i  # 记录商品的索引位置

        i += 1
    if pindex == -1:
        print('没有该商品的信息')


def updatebyid():
    # 从文件中获取文件信息
    productlist = readfiletolist()
    # print(productlist)

    if productlist == None or len(productlist) == 0:
        print('没有任何商品信息存在！')
        return

    id = input('请输入要修改的商品编号:')

    pindex = -1  # 找到商品字典对象在列表集合中的索引位置
    i = 0
    for pd in productlist:
        if pd['pid'] == id:
            pindex = i  # 记录商品的索引位置
            break
        i += 1
    if pindex != -1:
        product = productlist[pindex]
        print('修改前的商品信息如下:')
        print('%s\t\t %s\t\t %s\t\t %s\t\t\t%s' % (product['pid'], product['pname'], product['price'], product['num'], product['account']))

        product['pname'] = input('输入商品名称:')
        product['price'] = input('输入商品价格:')
        product['num'] = input('输入商品数量:')
        product['account'] = float(product['price']) * int(product['num'])

        writelisttofile(productlist)  # 讲更新后的商品重新写入文件
        print('更新成功！')
    else:
        print('更新失败!')

    pass


def deletebyid():
    # 从文件中获取文件信息
    productlist = readfiletolist()
    # print(productlist)

    if productlist == None or len(productlist) == 0:
        print('没有任何商品信息存在！')
        return
    pid = input('请输入要删除的商品编号:')

    pindex = -1  # 找到商品字典对象在列表集合中的索引位置
    i = 0
    for pd in productlist:
        if pd['pid'] == pid:
            pindex = i  # 记录商品的索引位置
            break

        i += 1
    if pindex != -1:
        product = productlist[pindex]
        print('删除前的商品信息如下:')
        print('%s\t\t %s\t\t %s\t\t %s\t\t\t%s' % (product['pid'], product['pname'], product['price'], product['num'], product['account']))

        productlist.remove(product)

        writelisttofile(productlist)  # 讲删除后的商品重新写入文件
        print('删除成功！')
    else:
        print('删除失败!')

    pass


'''
菜单
'''


def showmenu():
    while True:
        print('==' * 5, '商品库存管理', '==' * 5, '商品库存管理')
        print('=' * 60)
        print('1--新增')
        print('2--修改')
        print('3--删除')
        print('4--查找')
        print('5--显示')
        print('0--退出')
        print('=' * 60)
        choose = input('请输入您的选择:0-5之间的数字:')
        if choose == '1':
            print('商品库存管理>>商品增加>>')
            addproduct()
        if choose == '2':
            print('商品库存管理>>商品修改>>')
            updatebyid()
        if choose == '3':
            print('商品库存管理>>商品删除>>')
            deletebyid()
        if choose == '4':
            print('商品库存管理>>商品查找>>')
            findbyname()
        if choose == '5':
            print('商品库存管理>>商品显示>>')
            showproductlist()
        if choose == '0':
            print('谢谢使用，系统退出！')
            sys.exit(0)  # 调用退出系统方法


if __name__ == '__main__':
    showmenu()
    pass
