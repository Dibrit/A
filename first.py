from PyQt5.QtGui import QPainter, QColor, QPolygon
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton


class Artem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.qt = QPainter()
        self.status = None
        self.coords_ = [100, 100]
        self.flag = False
        self.convert_button = QPushButton(self)
        self.convert_button.setText('Сюда')
        self.convert_button.move(145, 10)
        self.convert_button.resize(25, 25)
        self.convert_button.clicked.connect(self.drawFlag())
        self.cbs = 1

    def initUI(self):
        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('Треугольник')

    def drawFlag(self):
        self.flag = True
        self.Paintevent()

    def Paintevent(self):
        if self.flag:
            self.qt = QPainter()
            self.qt.begin(self)
            self.setColor()
            self.draw()
            self.qt.end()

    def draw(self):
        size = randint(5, 150)
        self.qt.drawEllipse(*self.coords_, size, size)

    def setColor(self):
        self.qt.setBrush(QColor(25, 51, 0))


ex = Artem()
ex.show()