import sys
import random

from PyQt5.QtGui import QPolygon
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(1280, 900)
        self.pushButton = QPushButton(self)
        self.pushButton.resize(100, 50)
        self.pushButton.move(500, 800)
        self.pushButton.setText('новый круг')
        self.pushButton.clicked.connect(self.paint)

    def initUI(self):
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black']
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def drawing(self, qp):
        qp.setBrush(QColor(random.choice(self.colors)))
        a = randint(100, 600)
        qp.drawEllipse(400, 200, a, a)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Example()
    ex.show()
    exit(app.exec())
