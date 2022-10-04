import sys

from PyQt6.QtWidgets import QApplication, QWidget


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PyQt6')
        # self.setFixedHeight(400)
        # self.setFixedWidth(700)

        self.setStyleSheet('background-color: white')
        # self.setWindowOpacity(0.8)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
