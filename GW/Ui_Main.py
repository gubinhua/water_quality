# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GBH\Desktop\water_quality_access\water_quality\GW\Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 322)
        MainWindow.setMinimumSize(QtCore.QSize(524, 318))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_top = QtWidgets.QFrame(self.centralWidget)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_top.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_top)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comb_style = QtWidgets.QComboBox(self.frame_top)
        self.comb_style.setMinimumSize(QtCore.QSize(80, 20))
        self.comb_style.setObjectName("comb_style")
        self.comb_style.addItem("")
        self.comb_style.addItem("")
        self.horizontalLayout.addWidget(self.comb_style)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_open = QtWidgets.QPushButton(self.frame_top)
        self.btn_open.setAutoDefault(True)
        self.btn_open.setDefault(False)
        self.btn_open.setFlat(False)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout.addWidget(self.btn_open)
        self.label_path = QtWidgets.QLabel(self.frame_top)
        self.label_path.setMinimumSize(QtCore.QSize(120, 0))
        self.label_path.setObjectName("label_path")
        self.horizontalLayout.addWidget(self.label_path)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.frame_top)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_time = QtWidgets.QLabel(self.frame_top)
        self.label_time.setMinimumSize(QtCore.QSize(100, 0))
        self.label_time.setText("")
        self.label_time.setObjectName("label_time")
        self.horizontalLayout.addWidget(self.label_time)
        self.verticalLayout_4.addWidget(self.frame_top)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left = QtWidgets.QFrame(self.centralWidget)
        self.frame_left.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame_left)
        self.groupBox.setMinimumSize(QtCore.QSize(101, 101))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_preview = QtWidgets.QPushButton(self.groupBox)
        self.btn_preview.setAutoDefault(False)
        self.btn_preview.setDefault(False)
        self.btn_preview.setFlat(True)
        self.btn_preview.setObjectName("btn_preview")
        self.gridLayout.addWidget(self.btn_preview, 3, 0, 1, 1)
        self.btn_dataCheck = QtWidgets.QPushButton(self.groupBox)
        self.btn_dataCheck.setAutoDefault(False)
        self.btn_dataCheck.setDefault(False)
        self.btn_dataCheck.setFlat(True)
        self.btn_dataCheck.setObjectName("btn_dataCheck")
        self.gridLayout.addWidget(self.btn_dataCheck, 1, 0, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.groupBox)
        self.btn_save.setAutoDefault(False)
        self.btn_save.setDefault(False)
        self.btn_save.setFlat(True)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 4, 0, 1, 1)
        self.btn_viewDB = QtWidgets.QPushButton(self.groupBox)
        self.btn_viewDB.setAutoDefault(False)
        self.btn_viewDB.setDefault(False)
        self.btn_viewDB.setFlat(True)
        self.btn_viewDB.setObjectName("btn_viewDB")
        self.gridLayout.addWidget(self.btn_viewDB, 0, 0, 1, 1)
        self.btn_access = QtWidgets.QPushButton(self.groupBox)
        self.btn_access.setAutoDefault(False)
        self.btn_access.setDefault(False)
        self.btn_access.setFlat(True)
        self.btn_access.setObjectName("btn_access")
        self.gridLayout.addWidget(self.btn_access, 2, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.frame_left)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.frame_right = QtWidgets.QFrame(self.centralWidget)
        self.frame_right.setMinimumSize(QtCore.QSize(401, 241))
        self.frame_right.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right.setObjectName("frame_right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_right)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_right)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_welcom = QtWidgets.QLabel(self.page0)
        self.label_welcom.setObjectName("label_welcom")
        self.verticalLayout_6.addWidget(self.label_welcom)
        self.stackedWidget.addWidget(self.page0)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.page1)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.stackedWidget.addWidget(self.page3)
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.stackedWidget.addWidget(self.page4)
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.stackedWidget.addWidget(self.page5)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_right)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "水质评估"))
        self.label.setText(_translate("MainWindow", "评价类型："))
        self.comb_style.setItemText(0, _translate("MainWindow", "地下水"))
        self.comb_style.setItemText(1, _translate("MainWindow", "地表水"))
        self.btn_open.setText(_translate("MainWindow", "导入文件"))
        self.label_path.setText(_translate("MainWindow", "C:\\zhuomian11.xlsx"))
        self.label_3.setText(_translate("MainWindow", "当前时间："))
        self.groupBox.setTitle(_translate("MainWindow", "主功能区"))
        self.btn_preview.setText(_translate("MainWindow", "结果预览"))
        self.btn_dataCheck.setText(_translate("MainWindow", "数据核查"))
        self.btn_save.setText(_translate("MainWindow", "保存结果"))
        self.btn_viewDB.setText(_translate("MainWindow", "查看数据库"))
        self.btn_access.setText(_translate("MainWindow", "开始评估"))
        self.label_welcom.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#55ff00;\">欢迎使用水质评价系统</span></p></body></html>"))
        self.tableWidget.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

