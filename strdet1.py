import sys
import os
from strdet import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_5.clicked.connect(self.pdtls)
     self.ui.pushButton_2.clicked.connect(self.dplot)
     self.ui.pushButton_3.clicked.connect(self.gbc1)
     self.ui.pushButton_4.clicked.connect(self.bc1)
     self.ui.pushButton.clicked.connect(self.ecgf)
     

  def pdtls(self):
    os.system("python patient1.py")

  def dplot(self):
    os.system("python pie_chart1.py")

  def gbc1(self):
    os.system("python -W ignore gbc1.py")

  def bc1(self):
    os.system("python -W ignore bc1.py")

  def ecgf(self):
    os.system("python eyefeatures1.py")
	


          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
