import sys
import os
import json
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        #设置窗口初始位置和大小
        self.setGeometry(300,50,10,10)
        self.setWindowTitle('StackedWidget 例子')

        #创建列表窗口，添加条目
        self.leftlist=QListWidget()
        self.leftlist.insertItem(0,'联系方式')
        self.leftlist.insertItem(1,'个人信息')
        self.leftlist.insertItem(2,'教育程度')

        #创建三个小控件
        #self.stack0 = QWidget()
        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()
        #self.stack4=QWidget()
        #self.stack5=QWidget()

        #self.stack0UI()
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        #self.stack4UI()
       # self.stack5UI()

        #在QStackedWidget对象中填充了三个子控件
        self.stack=QStackedWidget(self)

        #self.stack.addWidget(self.stack0)
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        #self.stack.addWidget(self.stack4)
        #self.stack.addWidget(self.stack5)
        

        #垂直布局，添加部件到布局中
        HBox=QHBoxLayout()
        HBox.addWidget(self.leftlist)
        HBox.addWidget(self.stack)
        HBox.setStretch(1,3)
        self.setLayout(HBox)

        self.leftlist.currentRowChanged.connect(self.display)
    def stack1UI(self):
        layout=QHBoxLayout()
        dic = readDB('db.json')
        #print(dic)
        rows = len(dic.keys())
        col_names = list(dic[list(dic.keys())[0]].keys())
        print(col_names)
        cols = len(col_names)
        print(col_names[1])
        rows = len(dic[list(dic.keys())[0]].keys())
        print(rows)
        table = QTableWidget()
        table.setRowCount(rows)
        table.setColumnCount(cols)
        layout.addWidget(table)

        headers = ["编号","指标名称","计量单位",'Ⅰ类','Ⅱ类','Ⅲ类','Ⅳ类','Ⅴ类']
        row1 = ['','','','Ⅰ类','Ⅱ类','Ⅲ类','Ⅳ类','Ⅴ类']
        table.setHorizontalHeaderLabels(headers)


        for i in range(5):
            newItem = QTableWidgetItem()
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for row,item in enumerate(dic.keys()):
            for col,name in enumerate(col_names):
                print(dic[item][name])
                newItem = QTableWidgetItem(str(dic[item][name]))
                table.setItem(row,col,newItem)
        self.stack1.setLayout(layout)

    def stack2UI(self):
        # zhu表单布局，次水平布局
        layout = QFormLayout()
        sex = QHBoxLayout()

        # 水平布局添加单选按钮
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))

        # 表单布局添加控件
        layout.addRow(QLabel('性别'), sex)
        layout.addRow('生日', QLineEdit())

        self.stack2.setLayout(layout)

    def stack3UI(self):
        # 水平布局
        layout = QHBoxLayout()

        # 添加控件到布局中
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))

        self.stack3.setLayout(layout)
    def display(self,i):
        #设置当前可见的选项卡的索引
        self.stack.setCurrentIndex(i)

def readDB(dbpath):
    data_str = ''
    if os.path.exists(dbpath):
        with open(dbpath,'r',encoding='utf-8') as f:
            data_str = f.read()
            #print(data_str)
        dic = json.loads(data_str)
        print("数据库加载完成！")
        return dic
    else:
        print("找不到数据库文件！")  
        return None
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=StackedExample()
    demo.show()
    sys.exit(app.exec_())

# dic = {'001':{'id':001,'name':'jack'},'002':{'id':2,'name':'mack'}}
# print(type(list(dic.keys())))
# print(len(dic[list(dic.keys())[0]].keys()))