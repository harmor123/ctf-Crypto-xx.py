# -*- coding: utf-8 -*-
# Time: 2023/6/27 20:03
# Editor:harmor
import json
import sys

'''
读文件的函数
返回字典列表
'''


def readFileToList():
    # 从文件中获取学生成绩字典对象
    fp = open('grade.json', 'r', encoding='utf8')

    # 从文件中读取数据并转换为字典列表集合
    liststudent = json.load(fp)
    fp.close()
    return liststudent


# ===============================================================

'''
写文件的函数writeListToFile():
'''


def writeListToFile(slist: list):
    # 获取要操作的文件对象
    fp = open('grade.json', 'w', encoding='utf8')

    json.dump(slist, fp, ensure_ascii=False)
    print('文件写入成功！')
    fp.flush()
    fp.close()
    pass


'''
将添加的学生成绩信息保存到grade.json文件中
定义函数addStudent()
学生数据构成:
id--学号
name--姓名
chinese--语文
math--数学
english--英语
averrage--均分
'''


def addStudent():
    # 从文件中获取文件列表对象
    liststudent = readFileToList()

    # 从键盘输入学生的成绩
    student = {}
    student['id'] = input('请输入学生学号:')
    student['name'] = input('请输入学生姓名:')
    student['chinese'] = input('请输入语文成绩:')
    student['math'] = input('请输入数学成绩:')
    student['english'] = input('请输入英语成绩:')
    student['averrage'] = int(
        (float(student['chinese']) + float(student['math']) + float(student['english'])) / 3 + 0.5)

    liststudent.append(student)
    writeListToFile(liststudent)  # 调用写列表到文件的函数

    print('学生成绩添加成功！')
    pass


# ================================================================
'''
显示所有学生成绩的函数
定义函数showAllStudent()
'''


def showAllStudent():
    # 从文件中读取字典列表
    slist = readFileToList()

    # 判断字典列表中是否存在商品
    if slist == None or len(slist) == 0:
        print('系统中无任何数据存在！')
        return

    print('学号\t\t\t\t    姓名\t\t\t\t    语文\t\t\t\t    数学\t\t\t\t    英语\t\t\t\t    均分')
    print('=' * 110)
    for stu in slist:
        print('{0:<12}\t\t{1:<12}\t\t{2:<12}\t\t{3:<12}\t\t{4:<12}\t\t{5:<12}'.format(
            stu['id'], stu['name'], stu['chinese'], stu['math'], stu['english'], stu['averrage'], chr(12288)))
    print('=' * 110)

    pass


# ================================================================

'''
根据学生学号修改学生成绩信息并保存到store.json文件中
定义函数updateStudentt()
'''


def updateGrade():
    # 从文件中读取字典列表
    slist = readFileToList()

    # 判断字典列表中是否存在学生成绩信息
    if slist == None or len(slist) == 0:
        print('系统中无任何数据存在！')
        return

    index = -1  # 学生成绩信息对象在列表中的索引位置

    id = input('请输入要修改的学生学号：')

    # 在列表中查找是否存在该学生的列表对象
    # ======================================
    for i, student in enumerate(slist):
        if student['id'] == id:  # 找到该编号的学生成绩信息
            index = i  # 将索引位置传递给index
            break
    # ======================================

    if index != -1:
        stu = slist[index]  # 将索引位置处的学生对象传递给变量stu
        print('您要修改的学生成绩如下:')
        print('学号:%s\t\t    姓名:%s\t\t    语文:%s\t\t    数学:%s\t\t    英语:%s\t\t    均分:%s'
              % (stu['id'], stu['name'], stu['chinese'], stu['math'], stu['english'], stu['averrage']))
        print('请输入新的学生成绩：')
        stu['name'] = input('请输入学生姓名:')
        stu['chinese'] = input('请输入语文成绩:')
        stu['math'] = input('请输入数学成绩:')
        stu['english'] = input('请输入英语成绩:')
        stu['averrage'] = int((float(stu['chinese']) + float(stu['math']) + float(stu['english'])) / 3 + 0.5)

        # 将更改后的列表保存到文件中
        writeListToFile(slist)
        print('更新成功！')
    else:
        print('没有该学号的学生存在！修改失败！')

    pass


# ================================================================
'''
根据学生学号删除学生信息并保存到store.json文件中
定义函数delStudentById()
'''


def delStudentById():
    # 从文件中读取字典列表
    slist = readFileToList()

    # 判断字典列表中是否存在学生成绩信息
    if slist == None or len(slist) == 0:
        print('文件中无任何数据存在！')
        return

    index = -1  # 学生成绩信息对象在列表中的索引位置

    id = input('请输入要删除的学生学号：')

    # 在列表中查找是否存在该学生的列表对象
    # ======================================
    for i, student in enumerate(slist):
        if student['id'] == id:  # 找到该编号的学生成绩信息
            index = i  # 将索引位置传递给index
            break
    # ======================================

    if index != -1:
        stu = slist[index]  # 将索引位置处的学生成绩信息对象传递给变量stu
        print('您要删除的学生成绩如下:')
        print('学号:%s\t\t    姓名:%s\t\t    语文:%s\t\t    数学:%s\t\t    英语:%s\t\t    均分:%s'
              % (stu['id'], stu['name'], stu['chinese'], stu['math'], stu['english'], stu['averrage']))

        slist.remove(stu)  # 从列表中删除学生对象
        # 将更改后的列表保存到文件中
        writeListToFile(slist)  # 将更新以后的列表存储到文件
        print('删除成功！')
    else:
        print('没有该学号的学生存在！删除失败！')
    pass


# ===============================================================

'''
根据学生姓名从store.json文件中查询学生成绩
定义函数findStudentByName()
'''


def findStudentByName():
    # 从文件中读取字典列表
    slist = readFileToList()

    # 判断字典列表中是否存在学生成绩信息
    if slist == None or len(slist) == 0:
        print('文件中无任何数据存在！')
        return

    index = -1  # 学生成绩信息对象在列表中的索引位置

    searcherName = input('请输入要查询的学生姓名：')

    # 在列表中查找是否存在该学生的列表对象
    # ======================================
    for i, stu in enumerate(slist):
        if stu['name'] == searcherName:  # 找到该姓名的学生
            print('你要查询的学生成绩如下')
            print('学号:%s\t\t    姓名:%s\t\t    语文:%s\t\t    数学:%s\t\t    英语:%s\t\t    均分:%s'
                  % (stu['id'], stu['name'], stu['chinese'], stu['math'], stu['english'], stu['averrage']))
            index = i  # 将索引位置传递给index

    # ======================================

    if index == -1:
        print('没有该姓名的学生存在！')
    pass

    pass


# ==========================================================

'''
对各科目及班级平均分计算
定义函数calculate()
'''


def calculate():
    # 从文件中读取字典列表
    slist = readFileToList()

    # 判断字典列表中是否存在学生成绩信息
    if slist == None or len(slist) == 0:
        print('文件中无任何数据存在！')
        return

    index = -1  # 学生成绩信息对象在列表中的索引位置
    print('目前支持的计算科目为:')
    print('1.语文')
    print('2.数学')
    print('3.英语')
    print('4.班级均分')
    choose = input('请输入你要计算的科目的数字:')
    sub = ''
    if choose == '1':
        sub = 'chinese'
    if choose == '2':
        sub = 'math'
    if choose == '3':
        sub = 'english'
    if choose == '4':
        sub = 'averrage'
    # 在列表中查找是否存在该科目的列表对象
    # ======================================
    total = 0
    imin = 100
    imax = 0
    i = 0
    for i, stu in enumerate(slist):
        total = float(stu[sub]) + total  # 对该科目分数进行累加

        if imax < int(stu[sub]):
            imax = int(stu[sub])
        if imin > int(stu[sub]):
            imin = int(stu[sub])
    averrages = total / (i + 1)  # 计算均分
    print('你要计算的科目的均分为%.2f' % averrages)
    print('最高分：%d' % imax)
    print('最低分：%d' % imin)
    # ======================================

    pass


'''
定义菜单函数与用户交互
showMenu():
'''


def showMenu():
    while True:
        print('\t\t\t==学生期末成绩管理==')
        print('=' * 41)
        print('\t\t\t\t1--添加')
        print('\t\t\t\t2--修改')
        print('\t\t\t\t3--删除')
        print('\t\t\t\t4--查找')
        print('\t\t\t\t5--显示')
        print('\t\t\t\t6--均分计算')
        print('\t\t\t\t0--退出')
        print('=' * 41)
        choose = input('请输入您的选择0-6之间的数字：')
        if choose == '1':
            print('学生成绩管理>>添加>>')
            addStudent()  # 调用添加函数
        if choose == '2':
            print('学生成绩管理>>修改>>')
            updateGrade()
        if choose == '3':
            print('学生成绩管理>>删除>>')
            delStudentById()
        if choose == '4':
            print('学生成绩管理>>查找>>')
            findStudentByName()
        if choose == '5':
            print('学生成绩管理>>显示>>')
            showAllStudent()
        if choose == '6':
            print('学生成绩管理>>均分计算>>')
            calculate()
        if choose == '0':
            print('谢谢使用，系统退出！')
            sys.exit(0)

    pass


if __name__ == '__main__':
    showMenu()
    pass
