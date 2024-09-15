from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
window = QWidget()
window.resize(300,300)

text_label = QLabel("Натисніть на кнопку щоб знайти переможця")
win_label = QLabel("?")
button = QPushButton("Згенерувати")


layout = QVBoxLayout()
layout.addWidget(text_label, alignment= Qt.AlignCenter)
layout.addWidget(win_label, alignment= Qt.AlignCenter)
layout.addWidget(button, Qt.AlignCenter)

def winner():
    text_label.setText("Переможець")
    win_number = str(randint(1,100))
    win_label.setText(win_number)

button.clicked.connect(winner)

window.setLayout(layout)

window.show()
app.exec_()