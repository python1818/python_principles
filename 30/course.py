from turtle import onclick
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
import sys



def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Eren")
    win.setGeometry(00,100,1000,600)  
    win.setWindowIcon(QIcon("indir.jfif"))

    label_name = QLabel(win)
    label_name.setText("name : ")
    label_name.move(50, 30)
    label_surname = QLabel(win)
    label_surname.setText("surname : ")
    label_surname.move(50, 70)

    text_name =QLineEdit(win)
    text_name.move(120,30)
    text_surname= QLineEdit(win)
    text_surname.move(120,70)

    label_name_surname = QLabel(win)
    label_name_surname.move(120,200)
    label_name_surname.setText("Deneme")

    def onClick():
        print("clicked!!!" + text_name.text()+" " + text_surname.text())

    buton_save = QPushButton(win)
    buton_save.move(120,120)
    buton_save.setText("save it")
    buton_save.clicked.connect(onClick)

    win.show()
    sys.exit(app.exec_())

window()