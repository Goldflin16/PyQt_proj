from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
)
from PyQt5.QtCore import Qt

app = QApplication([0])
window = QWidget()
window.resize(320, 420)


app.setStyleSheet('''
                  QWidget {background-color: #939394}
                  QPushButton {background-color: #fcb500; font: 25px; color: #5e557a; border-radius: 10px}
                  QLabel {font: 25px}''')




result = QLabel("0")
b_0 = QPushButton("0")
b_1 = QPushButton("1")
b_2 = QPushButton("2")
b_3 = QPushButton("3")
b_4 = QPushButton("4")
b_5 = QPushButton("5")
b_6 = QPushButton("6")
b_7 = QPushButton("7")
b_8 = QPushButton("8")
b_9 = QPushButton("9")

b_plus = QPushButton("+")
b_minus = QPushButton("-")
b_multiply = QPushButton("*")
b_division = QPushButton("/")
b_equals = QPushButton("=")
b_point = QPushButton(".")
b_power = QPushButton("x^y")
b_backspace = QPushButton("<-")
b_clear = QPushButton("C")
b_percent = QPushButton("%")



b_0.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_2.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_3.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_4.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_5.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_6.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_7.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_8.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_9.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_plus.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_minus.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_multiply.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_division.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_equals.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_point.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_power.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_backspace.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_clear.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_percent.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

layout1 = QHBoxLayout()
layout1.addWidget(b_percent)
layout1.addWidget(b_0)
layout1.addWidget(b_point)
layout1.addWidget(b_equals)

layout2 = QHBoxLayout()
layout2.addWidget(b_1)
layout2.addWidget(b_2)
layout2.addWidget(b_3)
layout2.addWidget(b_plus)

layout3 = QHBoxLayout()
layout3.addWidget(b_4)
layout3.addWidget(b_5)
layout3.addWidget(b_6)
layout3.addWidget(b_minus)

layout4 = QHBoxLayout()
layout4.addWidget(b_7)
layout4.addWidget(b_8)
layout4.addWidget(b_9)
layout4.addWidget(b_multiply)

layout5 = QHBoxLayout()
layout5.addWidget(b_clear)
layout5.addWidget(b_backspace)
layout5.addWidget(b_power)
layout5.addWidget(b_division)

main_layout = QVBoxLayout()
main_layout.addWidget(result)
main_layout.addLayout(layout5)
main_layout.addLayout(layout4)
main_layout.addLayout(layout3)
main_layout.addLayout(layout2)
main_layout.addLayout(layout1)

window.setLayout(main_layout)


window.show()