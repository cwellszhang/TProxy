# -*- coding: utf-8 -*-

"""
Module implementing GraphClient.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
import sys
from  Ui_main import Ui_MainWindow


class GraphClient(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(GraphClient, self).__init__(parent)
        self.setupUi(self)
        self.ruleTable.setColumnCount(4)
        self.ruleTable.horizontalHeader().setVisible(True)
        self.ruleTable.setHorizontalHeaderLabels(['Type','Method','Url/IP', 'Rule']) 
        self.ruleTable.setColumnWidth(0, 117)
        self.ruleTable.setColumnWidth(1, 100)
        self.ruleTable.setColumnWidth(2, 300)
        self.ruleTable.setColumnWidth(3,  100)
        
    @pyqtSlot()
    def on_reqruleButton_clicked(self):
        """
        Slot documentation goes here.
        """
        url = self.urlText.text()
        method = self.methodSelect.currentText()
        rule = self.reqruleSelect.currentText()
        if url =='':
            QMessageBox.information(self,"Title"," Url Empty.", QMessageBox.Yes)
        else:
           currentRow=self.ruleTable.rowCount()
           self.ruleTable.insertRow(currentRow)
           typeItem=QTableWidgetItem('Request')
           self.ruleTable.setItem(currentRow, 0, typeItem)
           methodItem=QTableWidgetItem(method)
           self.ruleTable.setItem(currentRow, 1, methodItem)
           urlItem=QTableWidgetItem(url)
           self.ruleTable.setItem(currentRow, 2, urlItem)
           ruleItem=QTableWidgetItem(rule)
           self.ruleTable.setItem(currentRow, 3, ruleItem)
           
        
        
    
    @pyqtSlot()
    def on_resruleButton_clicked(self):
        """
        Slot documentation goes here.
        """
        ip = self.ipText.text()
        type= self.typeSelect.currentText()
        rule = self.resruleSelect.currentText()
        if ip =='':
            QMessageBox.information(self,"Title"," IP Empty.", QMessageBox.Yes)
        else:
           currentRow=self.ruleTable.rowCount()
           self.ruleTable.insertRow(currentRow)
           typeItem=QTableWidgetItem('Response')
           self.ruleTable.setItem(currentRow, 0, typeItem)
           tyItem=QTableWidgetItem(type)
           self.ruleTable.setItem(currentRow, 1, tyItem)
           ipItem=QTableWidgetItem(ip)
           self.ruleTable.setItem(currentRow, 2, ipItem)
           ruleItem=QTableWidgetItem(rule)
           self.ruleTable.setItem(currentRow, 3, ruleItem)
        pass
    
    @pyqtSlot()
    def on_removeButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.ruleTable.rowCount()==0:
            return
        mvrow = self.ruleTable.currentRow()
        msg = self.ruleTable.item(mvrow, 0)
        print(msg.text())
        self.ruleTable.removeRow(mvrow)
        

if __name__ == "__main__":
    app=QApplication(sys.argv)
    dlg=GraphClient()
    dlg.show()
    sys.exit(app.exec_())
    
    
