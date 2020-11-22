import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.drawbtn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.Color = QColor(randint(1, 255), randint(1, 255), randint(1, 255))
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        qp.setBrush(self.Color)
        a = randint(1, 330)
        qp.drawEllipse(70, 70, 70 + (340 - a), 70 + (340 - a))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())