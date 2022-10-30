import sys

from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage("Welcome")
window.menuBar().addMenu("File")

window.show()

sys.exit(app.exec())
