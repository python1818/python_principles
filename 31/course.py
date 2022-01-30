import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

def calculatorApp():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setWindowTitle("Hesap Makinesi")
    win.setGeometry(300,200,220,300)
    win.setWindowIcon(QIcon("C:/Users/istik/Desktop/pyhton/31/hesap.png"))

    label_num1 = QtWidgets.QLabel(win)
    label_num1.setText("Birinci Sayı :")
    label_num1.move(20,20)

    label_num2 = QtWidgets.QLabel(win)
    label_num2.setText("ikinci Sayı :")
    label_num2.move(20,60)
    
    label_result =QtWidgets.QLabel(win)
    label_result.setText("Sonuç :")
    label_result.move(20,260)

    label_result_2 = QtWidgets.QLabel(win)
    label_result_2.setText("")
    label_result_2.move(100,260)


    line_edit_num1 = QtWidgets.QLineEdit(win)
    line_edit_num1.move(100,20)
    line_edit_num1.resize(100,25)
      
    line_edit_num2 = QtWidgets.QLineEdit(win)
    line_edit_num2.move(100,60)
    line_edit_num2.resize(100,25)
    
    def add():
        result = int(line_edit_num1.text()) + int(line_edit_num2.text())
        label_result_2.setText(str(result))
    def subtract():
        result = int(line_edit_num1.text()) - int(line_edit_num2.text())
        label_result_2.setText(str(result))
    def multiply():
        result = int(line_edit_num1.text()) * int(line_edit_num2.text())
        label_result_2.setText(str(result))
    def divide():
        result = int(line_edit_num1.text()) / int(line_edit_num2.text())
        label_result_2.setText(str(result))


    button_add = QtWidgets.QPushButton(win)
    button_add.setText("Topla")
    button_add.move(100,100)
    button_add.clicked.connect(add)

    button_substract = QtWidgets.QPushButton(win)
    button_substract.setText("Çıkar")
    button_substract.move(100,140)
    button_substract.clicked.connect(subtract)
    
    button_multiply = QtWidgets.QPushButton(win)
    button_multiply.setText("Çarp")
    button_multiply.move(100,180)
    button_multiply.clicked.connect(multiply)

    button_divide = QtWidgets.QPushButton(win)
    button_divide.setText("böl")
    button_divide.move(100,220)
    button_divide.clicked.connect(divide)


    win.show()
    sys.exit(app.exec())




calculatorApp()