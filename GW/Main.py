# -*- coding: utf-8 -*-

"""
Module implementing Main.
"""
import sys
from PyQt5.QtCore import  QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem,  QAbstractItemView
from Ui_Main import Ui_MainWindow
import time
import pandas as pd
class TimeThread(QThread):
        update_date = pyqtSignal(str)
        def run(self):
            while True:
                date = QDateTime.currentDateTime()
                currentTime = date.toString("yyyy-MM-dd hh:mm:ss dddd")
                self.update_date.emit(str(currentTime))
                time.sleep(1)
class Main(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        
        super(Main, self).__init__(parent)
        
        timethread = TimeThread()
        timethread.update_date.connect(self.displayTime)
        timethread.start()
        
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
       
        self.btn_open.clicked.connect(self.importFile)
        self.btn_viewDB.clicked.connect(self.showTable)
        #self.comb_style.currentIndexChanged.connect(self.showDB)
    def displayTime(self, str):
        self.label_time.setText(str)
    
    def importFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "打开文件", "C:\\", "Excel Files(*.xlsx *.xls *.csv)")
        self.label_path.setText(filename)
        
    def showTable(self):
        self.showDB()
        self.stackedWidget.setCurrentIndex(1)
        
    def showDB(self):
        #self.tableWidget.setRowCount = 0
        #self.tableWidget.setColunmCount = 0
        dbpath = ""
        index = self.comb_style.currentIndex() 
        print(index)
        #地下水
        if index == 0:
            dbpath = '../db/gw.xlsx'
        elif index == 1:
            dbpath = '../db/sw.xlsx'
        data = pd.read_excel(dbpath)
        rows, cols = data.shape
        headers = data.columns.values
        print(headers)
        self.tableWidget.setRowCount (rows)
        self.tableWidget.setColumnCount(cols)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTrig8gers)
        #self.tableWidget.setTextAlignment(Qt.AlignHCenter)
        #self.tableWidget.setTextAlignment(Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderLabels(headers)
        
        for row in range(rows):
            values = data.loc[row].values
            for col in range(cols):
                newItem = QTableWidgetItem(str(values[col]))
                self.tableWidget.setItem(row,col,newItem)
        
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    ui  = Main()
    ui.show()
    sys, exit(app.exec())
    
        
        
