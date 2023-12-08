import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from UI import Ui_MainWindow
import random

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create_circle)

    def create_circle(self):
        scene = QGraphicsScene()
        view = QGraphicsView(scene)
        view.setGeometry(100, 100, 400, 400)
        diameter = random.randint(50, 150)
        ellipse = QGraphicsEllipseItem(0, 0, diameter, diameter)
        ellipse.setBrush(QColor(Qt.yellow))
        scene.addItem(ellipse)
        view.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())