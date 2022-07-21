class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def reset(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        self.ans = self.num1 + self.num2

    def mul(self):
        self.ans = self.num1 * self.num2

    def div(self):
        self.ans = self.num1 / self.num2

    def display(self):
        print(self.ans)

calc1 = Calculator(10, 20)
calc1.add()
calc1.display()
calc1.mul()
calc1.display()
calc1.reset(100, 20)
calc1.div()
calc1.display()