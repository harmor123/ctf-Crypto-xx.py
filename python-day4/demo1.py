# -*- coding: utf-8 -*-
# Time: 2023/6/7 8:52
# Editor:harmor


# -*- coding: utf-8 -*-
# Time: 2023/6/7 11:48
# Editor:harmor

import json
import sys
import os

'''
读取express.json文件并返回字典列表
'''


def readfile_to_list():
    fp = open('express.json', 'r', encoding='utf-8')
    if fp is None:
        print('文件没有内容！')
        return None
    else:
        list_express = json.load(fp)
        fp.close()  # 关闭文件
        return list_express


'''
向express.json文件写入文件
'''


def writelist_to_file(express_list: list):
    fp = open('express.json', 'w', encoding='utf-8')
    json.dump(express_list, fp, ensure_ascii=False)
    fp.flush()
    fp.close()  # 关闭文件


'''
添加快递信息的函数
'''


def add_express_information():
    # 从文件中获取文件信息
    express_list = readfile_to_list()

    if express_list is None:
        express_list = []

    # 创建商品字典对象
    express_information = {}

    # 从键盘输入字典数据
    express_information['id'] = input('请输入快递单号:')
    express_information['name1'] = input('请输入快递员姓名:')
    express_information['name2'] = input('请输入收件人姓名:')
    express_information['tel'] = input('请输入收件人电话(11位):')
    express_information['address1'] = input('请输入收件人地址(15字以内):')
    express_information['address2'] = input('请输入寄件人地址(15字以内):')
    express_information['type'] = input('请输入快递的类型(普通快递、特快专递):')
    express_information['state'] = input('请输入快递的状态(已发货、派送中、已签收):')
    express_information['notes'] = input('请输入快递的备注:')

    express_list.append(express_information)  # 添加商品到商品集合

    # 写入集合到文件
    writelist_to_file(express_list)
    print('快递信息添加成功！')
    pass


'''
查询快递信息的函数1:根据快递单号查询快递信息
'''


def find_express_information_by_id():
    # 从文件中获取文件信息
    express_list = readfile_to_list()
    # print(express_list)

    if express_list is None or len(express_list) == 0:
        print('没有任何快递信息存在！')
        return

    pid = input('输入要查询快递的快递单号:')
    pindex = -1  # 找到快递字典对象在列表集合中的索引位置
    i = 0
    for pd in express_list:
        if pd['id'] == pid:
            print('找到的快递信息如下:')
            print(
                '{0:<7}\t\t{1:<9}\t\t{2:<9}\t\t{3:<10}\t\t{4:<35}\t\t{5:<36}\t\t{6:<10}\t\t{7:<10}\t\t{8:<10}\t\t'.format(
                    '快递单号', '快递员姓名', '收件人姓名', '收件人电话', '收件人地址', '寄件人地址', '快递类型',
                    '快递状态', '快递备注', chr(12288)))
            print('=' * 230)
            print(
                '{0:<10}\t\t{1:<12}\t\t{2:<12}\t\t{3:<15}\t\t{4:<30}\t\t{5:<30}\t\t{6:<10}\t\t{7:<10}\t\t{8:<20}\t\t'.format(
                    pd['id'], pd['name1'], pd['name2'], pd['tel'], pd['address1'], pd['address2'], pd['type'],
                    pd['state'], pd['notes'], chr(12288)))
            pindex = i  # 记录快递信息的索引位置
        i += 1
    if pindex == -1:
        print('没有该快递的信息')

    pass


'''
查询快递信息的函数2:根据收件人电话查询快递信息
'''


def find_express_information_by_telephone():
    # 从文件中获取文件信息
    express_list = readfile_to_list()
    # print(express_list)

    if express_list is None or len(express_list) == 0:
        print('没有任何快递信息存在！')
        return

    ptel = input('输入要查询快递的收件人电话(11位):')
    pindex = -1  # 找到快递字典对象在列表集合中的索引位置
    i = 0
    for pd in express_list:
        if pd['tel'] == ptel:
            print('找到的快递信息如下:')
            print(
                '{0:<7}\t\t{1:<9}\t\t{2:<9}\t\t{3:<10}\t\t{4:<35}\t\t{5:<36}\t\t{6:<10}\t\t{7:<10}\t\t{8:<10}\t\t'.format(
                    '快递单号', '快递员姓名', '收件人姓名', '收件人电话', '收件人地址', '寄件人地址', '快递类型',
                    '快递状态', '快递备注', chr(12288)))
            print('=' * 230)
            print(
                '{0:<10}\t\t{1:<12}\t\t{2:<12}\t\t{3:<15}\t\t{4:<30}\t\t{5:<30}\t\t{6:<10}\t\t{7:<10}\t\t{8:<20}\t\t'.format(
                    pd['id'], pd['name1'], pd['name2'], pd['tel'], pd['address1'], pd['address2'], pd['type'],
                    pd['state'], pd['notes'], chr(12288)))
            pindex = i  # 记录快递信息的索引位置
        i += 1
    if pindex == -1:
        print('没有该快递的信息')
    pass


'''
根据快递单号修改快递信息的函数(更改快递员姓名、收件人地址、联系电话、快递的类型、快递的状态、快递的备注)
'''


def update_express_information_by_id():
    # 从文件中获取文件信息
    express_list = readfile_to_list()
    # print(express_list)

    if express_list is None or len(express_list) == 0:
        print('没有任何快递信息存在！')
        return

    pid = input('请输入要修改的快递信息的快递单号:')

    pindex = -1  # 找到商品字典对象在列表集合中的索引位置
    i = 0
    for pd in express_list:
        if pd['id'] == pid:
            pindex = i  # 记录商品的索引位置
            break
        i += 1
    if pindex != -1:
        express = express_list[pindex]
        print('修改前的快递信息如下:')
        print(
            '{0:<7}\t\t{1:<9}\t\t{2:<9}\t\t{3:<10}\t\t{4:<35}\t\t{5:<36}\t\t{6:<10}\t\t{7:<10}\t\t{8:<10}\t\t'.format(
                '快递单号', '快递员姓名', '收件人姓名', '收件人电话', '收件人地址', '寄件人地址', '快递类型',
                '快递状态', '快递备注', chr(12288)))
        print('=' * 230)
        print(
            '{0:<10}\t\t{1:<12}\t\t{2:<12}\t\t{3:<15}\t\t{4:<30}\t\t{5:<30}\t\t{6:<10}\t\t{7:<10}\t\t{8:<20}\t\t'.format(
                express['id'], express['name1'], express['name2'], express['tel'], express['address1'],
                express['address2'], express['type'], express['state'], express['notes'], chr(12288)))

        express['name1'] = input('请输入新的快递员姓名:')
        express['name2'] = input('请输入新的收件人姓名:')
        express['tel'] = input('请输入新的收件人电话(11位):')
        express['address1'] = input('请输入新的收件人地址(15字以内):')
        express['type'] = input('请输入新的快递类型(普通快递、特快专递):')
        express['state'] = input('请输入新的快递状态(已发货、派送中、已签收):')
        express['notes'] = input('请输入新的快递备注:')

        writelist_to_file(express_list)  # 讲更新后的快递信息重新写入文件
        print('更新成功！')
    else:
        print('更新失败!')

    pass


'''
根据快递单号删除快递信息的函数
'''


def delete_express_information_by_id():
    # 从文件中获取文件信息
    express_list = readfile_to_list()
    # print(express_list)

    if express_list is None or len(express_list) == 0:
        print('没有任何快递信息存在！')
        return

    pid = input('请输入要删除的快递信息的快递单号:')
    pindex = -1  # 找到快递信息字典对象在列表集合中的索引位置
    i = 0
    for pd in express_list:
        if pd['id'] == pid:
            pindex = i  # 记录快递信息的索引位置
            break

        i += 1
    if pindex != -1:
        express = express_list[pindex]
        print('删除前的快递信息如下:')
        print(
            '{0:<7}\t\t{1:<9}\t\t{2:<9}\t\t{3:<10}\t\t{4:<35}\t\t{5:<36}\t\t{6:<10}\t\t{7:<10}\t\t{8:<10}\t\t'.format(
                '快递单号', '快递员姓名', '收件人姓名', '收件人电话', '收件人地址', '寄件人地址', '快递类型',
                '快递状态', '快递备注', chr(12288)))
        print('=' * 230)
        print(
            '{0:<10}\t\t{1:<12}\t\t{2:<12}\t\t{3:<15}\t\t{4:<30}\t\t{5:<30}\t\t{6:<10}\t\t{7:<10}\t\t{8:<20}\t\t'.format(
                express['id'], express['name1'], express['name2'], express['tel'], express['address1'],
                express['address2'], express['type'], express['state'], express['notes'], chr(12288)))

        express_list.remove(express)  # 使用remove函数删除快递信息

        writelist_to_file(express_list)  # 将删除后剩下的快递信息重新写入文件
        print('删除成功！')
    else:
        print('删除失败!')

    pass


'''
显示所有的快递信息
'''


def show_express_information():
    # 从文件中获取文件信息
    express_list = readfile_to_list()
    # print(express_list)

    if express_list is None or len(express_list) == 0:
        print('没有任何快递信息存在！')
        return
    # 输出快递信息
    print('*************' * 8, ' 商品库存信息 ', '*************' * 8, )
    print(
        '{0:<7}\t\t{1:<9}\t\t{2:<9}\t\t{3:<10}\t\t{4:<35}\t\t{5:<36}\t\t{6:<10}\t\t{7:<10}\t\t{8:<10}\t\t'.format(
            '快递单号', '快递员姓名', '收件人姓名', '收件人电话', '收件人地址', '寄件人地址', '快递类型',
            '快递状态', '快递备注', chr(12288)))
    print('=' * 230)
    for pd in express_list:
        print(
            '{0:<10}\t\t{1:<12}\t\t{2:<12}\t\t{3:<15}\t\t{4:<30}\t\t{5:<30}\t\t{6:<10}\t\t{7:<10}\t\t{8:<20}\t\t'.format(
                pd['id'], pd['name1'], pd['name2'], pd['tel'], pd['address1'], pd['address2'], pd['type'],
                pd['state'], pd['notes'], chr(12288)))
    pass


'''
菜单栏
'''


def show_menu():
    while True:
        print('##' * 10, '快递信息管理', '##' * 10)
        print('-' * 60)
        print('1--新增')
        print('2--查找(通过快递单号)')
        print('3--查找(通过收件人电话)')
        print('4--删除')
        print('5--修改')
        print('6--显示')
        print('0--退出')
        print('-' * 60)
        choose = input('请输入您的选择(0-6之间的数字):')
        if choose == '1':
            print('快递信息管理>>快递信息增加>>')
            add_express_information()
        if choose == '2':
            print('快递信息管理>>通过快递单号查找快递信息>>')
            find_express_information_by_id()
        if choose == '3':
            print('快递信息管理>>通过收件人电话查找快递信息>>')
            find_express_information_by_telephone()
        if choose == '4':
            print('快递信息管理>>快递信息删除>>')
            delete_express_information_by_id()
        if choose == '5':
            print('快递信息管理>>快递信息更新>>')
            update_express_information_by_id()
        if choose == '6':
            print('快递信息管理>>快递信息显示>>')
            show_express_information()
        if choose == '0':
            print('系统退出,谢谢使用！')
            sys.exit(0)  # 调用退出系统方法

    pass


if __name__ == '__main__':
    show_menu()  # 显示菜单
    pass






