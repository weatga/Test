import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5 import uic
import random

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.create_circle)

    def create_circle(self):
        scene = QGraphicsScene()
        diameter = random.randint(50, 150)
        ellipse = QGraphicsEllipseItem(0, 0, diameter, diameter)
        ellipse.setBrush(QColor(Qt.yellow))
        scene.addItem(ellipse)
        self.graphicsView.setScene(scene)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())