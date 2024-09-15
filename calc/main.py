from calc_layout import *

class Calc():
    def __init__(self, *args):
        self.point = 0
        self.actions = False
        self.actions = ["+", "-", "/", "*"]

    def push_1(self):
        if result.text() == "0":
            result.setText("1")
        else:
            result.setText(result.text() + "1")
    def push_2(self):
        if result.text() == "0":
            result.setText("2")
        else:
            result.setText(result.text() + "2")
    def push_3(self):
        if result.text() == "0":
            result.setText("3")
        else:
            result.setText(result.text() + "3")
    def push_4(self):
        if result.text() == "0":
            result.setText("4")
        else:
            result.setText(result.text() + "4")
    def push_5(self):
        if result.text() == "0":
            result.setText("5")
        else:
            result.setText(result.text() + "5")
    def push_6(self):
        if result.text() == "0":
            result.setText("6")
        else:
            result.setText(result.text()+ "6")
    def push_7(self):
        if result.text() == "0":
            result.setText("7")
        else:
            result.setText(result.text()+ "7")
    def push_8(self):
        if result.text() == "0":
            result.setText("8")
        else:
            result.setText(result.text()+ "8")
    def push_9(self):
        if result.text() == "0":
            result.setText("9")
        else:
            result.setText(result.text()+ "9")
   

    def push_point(self):
        if self.point == 0:
            result.setText(result.text() + ".")
            self.point = 1
        elif self.point == 1 and self.action:
            result.setText(result.text()+ ".")
            self.point = 2

    def push_plus(self):
        if not self.action:
            result.setText(result.text() + "+")
            self.actions = True
        elif result.text() [-1] in self.actions:
            result.setText(result.text()[:-1] + "+")


calc = Calc()

b_1.clicked.connect(calc.push_1)
b_2.clicked.connect(calc.push_2)
b_3.clicked.connect(calc.push_3)
b_4.clicked.connect(calc.push_4)
b_5.clicked.connect(calc.push_5)
b_6.clicked.connect(calc.push_6)
b_7.clicked.connect(calc.push_7)
b_8.clicked.connect(calc.push_8)
b_9.clicked.connect(calc.push_9)


b_point.clicked.connect(calc.push_point)
b_point.clicked.connect(calc.push_1)




app.exec_()