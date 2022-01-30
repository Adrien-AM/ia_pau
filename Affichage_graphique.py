import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 250))
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Revendication du brevet :')
        self.nameLabel.resize(172, 32)
        self.nameLabel.move(164, 20)

        self.line = QLineEdit(self)
        self.line.resize(200, 32)
        self.line.move(150, 60)


        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(150, 120)

        self.Lab = QLabel(self)
        self.Lab.setText('Résultats :')
        self.Lab.resize(70,32)
        self.Lab.move(215,170)

        self.Lab2 = QLabel(self)
        self.Lab2.resize(70, 32)
        self.Lab2.move(235, 170)


    def clickMethod(self):
        #On renvoie les données recuperer
        print('Ta référence de brevet: ' + self.line.text())
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )