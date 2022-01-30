import sys
import fasttext
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(800, 300))
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Revendication du brevet :')
        self.nameLabel.resize(172, 32)
        self.nameLabel.move(314, 20)

        self.line = QLineEdit(self)
        self.line.resize(200, 32)
        self.line.move(300, 60)


        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(300, 120)

        self.Lab = QLabel(self)
        self.Lab.setText('Résultats :')
        self.Lab.resize(70,32)
        self.Lab.move(365,170)

        self.Lab2 = QLabel(self)
        self.Lab2.resize(290, 32)
        self.Lab2.move(255, 210)

        self.Lab3 = QLabel(self)
        self.Lab3.resize(290, 32)
        self.Lab3.move(255, 250)

    def clickMethod(self):
        #On renvoie les données recuperer
        a,b = model.predict(self.line.text(),k=2)
        ##print(model.predict(self.line.text(), k=2))
        self.Lab2.setText("Classe : "+a[0][9]+a[0][10]+a[0][11]+" avec une probabilité de : "+str(round(b[0],2)))
        self.Lab3.setText("Classe : "+a[1][9]+a[1][10]+a[1][11]+" avec une probabilité de : "+str(round(b[1],2)))
        

if __name__ == "__main__":
    model = fasttext.load_model("modelFR/modelFR.bin")
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
"""
Appareil électrique selon l'une quelconque des revendications précédentes, caractérisé en ce que le nombre d'orifices correspond au nombre d'unités de moyens de connexions.
"""
