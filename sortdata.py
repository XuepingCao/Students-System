'''
排序模块：
根据英语成绩、Python成绩、C语言成绩和总成绩按升序或降序排列
'''

#coding=utf-8
import os
from search_total import show, show_student

filename="student.txt"
def sort():
    show()
    if os.path.exists(filename):           #判断文件是否存在
        student_new=[]
        with open(filename,'r') as rfile:  #打开文件
            student_old=rfile.readlines()
        for student_info in student_old:
            student_new.append(dict(eval(student_info)))  #将转换后的字典添加到列表中
    else:
        return
    ascORdesc=input("请选择(0升序；1降序)：")
    if ascORdesc=='0':                    #按升序排序
        ascORdescBool=False
    elif ascORdesc=='1':                  #按降序排序
        ascORdescBool=True
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode=input("请选择排序方式(1按英语成绩排序；2按Python成绩排序；3按C语言成绩排序；0按总成绩排序)：")
    if mode=='1':
        student_new.sort(key=lambda x: x["English"],reverse=ascORdescBool)
    elif mode=='2':
        student_new.sort(key=lambda x: x["Python"],reverse=ascORdescBool)
    elif mode=='3':
        student_new.sort(key=lambda x: x["C"],reverse=ascORdescBool)
    elif mode=='0':
        student_new.sort(key=lambda x: x["English"] + x["Python"] + x["C"],reverse=ascORdescBool)
    else:
        print("您输入有误，请重新输入！")
        sort()
    show_student(student_new)                 #显示排序结果

