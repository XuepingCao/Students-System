#coding=utf-8
'''
查询/统计模块
1.根据学生编号或姓名查找学生信息
2.统计学生总人数和显示所有学生信息
'''
import os

filename="student.txt"
#查询学生信息
def search():
    mark=True
    student_query=[]                 #保存查询结果的学生列表
    while mark:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input("按ID查询输入1；按姓名查询输入2：")
            if mode=="1":
                id=input("请输入学生ID: ")    #按学生编号查询
            elif mode=="2":
                name=input("请输入学生姓名：")  #按学生姓名查询
            else:
                print("您的输入有误，请重新输入！")
                search()                      #重新重新
            with open(filename,'r') as rfile:     #打开文件
                student_data=rfile.readlines()    #读取全部内容
                for student_info in student_data:
                    student_dict=dict(eval(student_info))  #字符串转字典
                    if id != "":               #判断是否按ID查询
                        if student_dict['id']==id: 
                            student_query.append(student_dict) #将找到的学生信息保存到列表中
                    elif name != "":           #判断是否按name查询
                        if student_dict['name']==name:
                            student_query.append(student_dict)
                show_student(student_query)            #显示查询结果
                student_query.clear()                  #清空列表
                inputMark=input("是否继续查询？(y/n)：")
                if inputMark=='y':
                    mark=True
                else:
                    mark=False
        else:
            print("暂未保存数据信息...")
            return

#将保存在列表中的学生信息显示出来
def show_student(studentList):
    if not studentList:                       #如果没有要显示的数据
        print("无数据信息！")
        return
    #定义标题显示格式
    title="{:^6}{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^10}"       #数字表示所占宽度，符号“^”表示居中显示，"\t"表示添加一个制表符
    print(title.format("ID","姓名","英语成绩","Python成绩","C语言成绩","总成绩"))  #按指定格式显示标题
    #定义具体内容显示格式
    data="{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:                  #通过for循环将列表中的数据全部显示出来
        print(data.format(info.get("id"),
            info.get("name"),str(info.get("English")),str(info.get("Python")),str(info.get("C")),
            str(info.get("English") + info.get("Python") + info.get("C")).center(12)))  #center()返回宽度为12的字符串


#实现统计学生总人数功能
def total():
    if os.path.exists(filename):               #判断文件是否存在
        with open(filename,'r') as rfile:      #打开文件
            student_old=rfile.readlines()
            if student_old:
                print("一共有 %d 名学生！"% len(student_old))   #统计学生人数
            else:
                print("还没有录入学生信息！")
    else:
        print("暂未保存数据信息！")


#显示所有学生信息
def show():
    student_new=[]
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            student_old=rfile.readlines()
        for student_info in student_old:
            student_new.append(eval(student_info))
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息！")


