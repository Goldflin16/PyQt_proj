from calc_layout import *

class Calc():
    def __init__(self, *args):
        self.point = 0
        self.action = False
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
            if result.text()[-1] in self.actions: 
                result.setText(result.text() + "0.")
            else:
                result.setText(result.text() + ".")
            self.point = 2

    def push_plus(self):
        if not self.action:
            if result.text()[-1] == ".":
                result.setText(result.text()[:-1] + "+") 
            else:
                result.setText(result.text() + "+")
            self.actions = True
            self.point = 1
        elif result.text() [-1] in self.actions:
            result.setText(result.text()[:-1] + "+")


    def push_minus(self):
        if not self.action:
            if result.text()[-1] == "-":
                result.setText(result.text()[:-1] + "-") 
            else:
                result.setText(result.text() + "-")
            self.actions = True
            self.point = 1
        elif result.text() [-1] in self.actions:
            result.setText(result.text()[:-1] + "-")


    def push_division(self):
        if not self.action:
            if result.text()[-1] == "/":
                result.setText(result.text()[:-1] + "/") 
            else:
                result.setText(result.text() + "/")
            self.actions = True
            self.point = 1
        elif result.text() [-1] in self.actions:
            result.setText(result.text()[:-1] + "/")


    def push_multiply(self):
        if not self.action:
            if result.text()[-1] == "*":
                result.setText(result.text()[:-1] + "*") 
            else:
                result.setText(result.text() + "*")
            self.actions = True
            self.point = 1
        elif result.text() [-1] in self.actions:
            result.setText(result.text()[:-1] + "*")

    def push_clear(self):
        result.setText("0")
        self.action = False
        self.point = 0

    def push_backspace(self):
        if result.text()[-1] == ".":
            self.point -= 1
        if result.text()[-1] in self.actions:
            self.action = False
        result.setText(result.text()[:1])
        if len(result.text()) == 0:
            result.setText("0")



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
b_plus.clicked.connect(calc.push_plus)
b_minus.clicked.connect(calc.push_minus)
b_division.clicked.connect(calc.push_division)
b_multiply.clicked.connect(calc.push_multiply)
b_clear.clicked.connect(calc.push_clear)
b_backspace.clicked.connect(calc.push_backspace)






app.exec_()