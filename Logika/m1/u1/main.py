from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Визначник переможця')
main_win.move(100, 100)
main_win.resize(400, 200)
main_win.show()

button = QPushButton('Згенерувати')
text = QLabel('Натисніть щоб згенерувати рандомне число')

app.exec_()
