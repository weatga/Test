import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QWidget, QGraphicsEllipseItem, QPushButton, QVBoxLayout, QGraphicsView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import random

class CircleDrawer:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget(self.window)
        layout = QVBoxLayout(central_widget)

        self.button = QPushButton('Draw Circle')
        self.graphics_view = QGraphicsView()
        layout.addWidget(self.button)
        layout.addWidget(self.graphics_view)

        self.button.clicked.connect(self.create_circle)

        self.window.setCentralWidget(central_widget)
        self.window.setGeometry(100, 100, 400, 300)
        self.window.show()

    def create_circle(self):
        scene = QGraphicsScene()
        diameter = random.randint(50, 150)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        ellipse = QGraphicsEllipseItem(0, 0, diameter, diameter)
        ellipse.setBrush(color)
        scene.addItem(ellipse)

        self.graphics_view.setScene(scene)

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    circle_drawer = CircleDrawer()
    circle_drawer.run()