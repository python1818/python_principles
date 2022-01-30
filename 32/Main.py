import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow


class mycalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(mycalculator,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.B_1.clicked.connect(self.add)
        self.ui.B_2.clicked.connect(self.substract)
        self.ui.B_3.clicked.connect(self.multiply)
        self.ui.B_4.clicked.connect(self.divide)

    def substract(self):
        result = int(self.ui.lineEdit.text()) - int(self.ui.lineEdit_2.text())
        self.ui.label_4.setText(str(result))

    def multiply(self):
        result = int(self.ui.lineEdit.text()) * int(self.ui.lineEdit_2.text())
        self.ui.label_4.setText(str(result))

    def divide(self):
        result = int(self.ui.lineEdit.text()) / int(self.ui.lineEdit_2.text())
        self.ui.label_4.setText(str(result))


    def add(self):
        result = int(self.ui.lineEdit.text()) + int(self.ui.lineEdit_2.text())
        self.ui.label_4.setText(str(result))


app = QtWidgets.QApplication(sys.argv)
win = mycalculator()
win.show()
sys.exit(app.exec_())