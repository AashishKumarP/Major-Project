import sys
from patient import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
con = sqlite3.connect('strdet1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues) 

   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        pid = str(self.ui.lineEdit_3.text())
        name = str(self.ui.lineEdit_4.text())
        addr1 = str(self.ui.lineEdit_5.text())
        addr2 = str(self.ui.lineEdit_6.text())
        adhar = str(self.ui.lineEdit.text())	
        mobile = str(self.ui.lineEdit_2.text())
        age = str(self.ui.lineEdit_7.text())
        cur.execute('INSERT INTO patient VALUES(?,?,?,?,?,?,?)',(pid,name,age,addr1,addr2,adhar,mobile))
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


