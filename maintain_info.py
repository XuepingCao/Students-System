#coding=utf-8
'''
学生信息维护模块：
1.录入学生信息
2.删除学生信息
3.修改学生信息
'''
import os
from search_total import show

filename="student.txt"
#将学生信息保存到文件
def save(student): 
    try:
        students_txt=open(filename,'a')       #以追加模式打开
    except Exception as e:
        students_txt=open(filename,'w')       #文件不存在，创建文件并打开
    for info in student:
        students_txt.write(str(info) + "\n")  #按行存储，添加换行符
    students_txt.close()                      #关闭文件


#录入学生信息
def insert():
    studentList=[]                            #保存学生信息的列表
    mark=True                                 #设置一个标记变量mark，用于控制是否退出循环,是否继续添加
    while mark:
        id=input("请输入ID(如：1001)：")
        if not id:                            #ID为空，跳出循环
            break
        name=input("请输入姓名：")
        if not name:                          #name为空，跳出循环
            break
        try:
            english=int(input("请输入英语成绩："))
            python=int(input("请输入python成绩："))
            c=int(input("请输入C语言成绩："))
        except:
            print("输入无效，不是整型数值，请重新录入信息")
            continue
        #将输入的学生信息保存到字典
        student={"id":id,"name":name,"English":english,"Python":python,"C":c}
        studentList.append(student)          #将学生字典添加到列表中
        inputMark=input("是否继续添加？ (y/n):")
        if inputMark=="y":                   #继续添加
            mark=True
        else:
            mark=False                       #不继续添加
    save(studentList)
    print("学生信息录入完毕！")


#删除学生信息
def delete():
    mark=True                                #标记是否循环
    while mark:
        studentId=input("请输入要删除的学生ID: ")
        if studentId != "":              #判断是否输入要删除的学生
            if os.path.exists(filename):     #判断文件是否存在
                with open(filename,'r') as rfile:  #打开文件
                    student_old=rfile.readlines()  #读取全部内容
            else:
                student_old=[]
        ifdel=False                          #标记是否删除
        if student_old:                      #如果存在学生信息
            with open(filename,'w') as wfile: #以写入方式打开文件
                student_dict={}              #定义空字典
                for student_info in student_old: 
                    student_dict=dict(eval(student_info))  #字符串转字典
                    if student_dict['id']!=studentId:
                        wfile.write(str(student_dict) + "\n") #将一条学生信息写入文件
                    else:
                        ifdel=True                            #标记已经删除
                if ifdel:
                    print("ID为 %s 的学生信息已经被删除..." % studentId)
                else:
                    print("没有找到ID为 %s 的学生信息..." % studentId)
        else:                                #不存在学生信息
            print("无学生信息...")
            break                            #退出循环
        show()
        inputMark=input("是否继续删除？ (y/n):")
        if inputMark=='y':
            mark=True                        #继续删除
        else:
            mark=False                       #退出删除学生信息功能


#修改学生信息
def modify():
    show()
    if os.path.exists(filename):              #判断文件是否存在
        with open(filename,'r') as rfile:     #打开文件
            student_old=rfile.readlines()     #读取全部信息
    else:
        return
    studentId=input("请输入要修改的学生ID：")
    with open(filename,'w') as wfile:          #以只写模式打开文件
        student_dict={}
        for student_info in student_old:
            student_dict=dict(eval(student_info)) #将字符串转字典
            if student_dict["id"]==studentId:     #是否为要修改的学生
                print("找到了这名学生，可以修改他的信息！")
                while True:                       #输入要修改的信息
                    try:
                        student_dict["id"]=input("请输入ID：")
                        student_dict["name"]=input("请输入姓名：")
                        student_dict["English"]=int(input("请输入英语成绩："))
                        student_dict["Python"]=int(input("请输入Python成绩："))
                        student_dict["C"]=int(input("请输入C语言成绩："))
                    except:
                        print("您的输入有误，请重新输入！")
                    else:
                        break
                wfile.write(str(student_dict) + "\n")  #将字典转为字符串，并写入文件
                print("修改成功")
            else:
                wfile.write(str(student_dict) + "\n")           #将未修改的信息写入文件
    mark=input("是否继续修改其他学生信息？ (y/n):")
    if mark=="y":
        modify()                                   #重新执行修改操作


