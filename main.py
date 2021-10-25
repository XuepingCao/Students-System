'''
主函数
运行学生信息管理系统，进入主功能菜单的选择界面，用户根据需要输入要执行功能对应的数字编号，进入对应的子功能中去。
'''

import re
from maintain_info import insert,delete,modify
from search_total import search,total,show
from sortdata import sort

def menu():
    #输出菜单
    print('''
    |————————————学生信息管理系统—————————————|
    |     ========== 功能菜单 ==========      |
    |     1  登入学生信息                     |
    |     2  查找学生信息                     |
    |     3  删除学生信息                     |
    |     4  修改学生信息                     |
    |     5  排序                             │
    |     6  汇总学生总人数                   |
    |     7  显示所有学生信息                 |
    |     0  退出系统                         |
    |     ===============================     |
    |     说明：通过数字选择菜单              |
    |________________________________________ |
    ''')


def main():
    ctrl=True   #标记是否退出系统
    while ctrl:
        menu()
        option=input("请选择：")              #选择菜单项
        option_str=re.sub("\D","",option)    #提取数字
        if option_str in ['0','1','2','3','4','5','6','7']:
            option_int=int(option_str)
            if option_int==0:                #退出系统
                print("您已退出学生管理系统！")
                ctrl=False
            elif option_int==1:              #录入学生成绩信息
                insert()
            elif option_int==2:              #查找学生成绩信息
                search()
            elif option_int==3:              #删除学生成绩信息
                delete()
            elif option_int==4:              #修改学生成绩信息
                modify()
            elif option_int==5:              #排序
                sort()
            elif option_int==6:              #统计学生总人数
                total()
            elif option_int==7:              #显示学生所有信息
                show()

#创建程序入口，调用主函数
if __name__=='__main__':
    main()

