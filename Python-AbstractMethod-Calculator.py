from abc import abstractmethod

class Calculator:
    __num1 = None
    __num2 = None
    __ans = None

    def __init__(self, num1, num2):
        try:
            self.__num1 = int(num1)
            self.__num2 = int(num2)
        except:
            print("Invalid entry")
            exit()
        
    @property
    def num1(self):
        return self.__num1

    @property
    def num2(self):
        return self.__num2

    @property
    def ans(self):
        return self.__ans

    @num1.setter
    def num1(self, val):
        self.__num1 = val

    @num2.setter
    def num2(self, val):
        self.__num2 = val

    @ans.setter
    def ans(self, val):
        self.__ans = val

    @abstractmethod
    def calculate(self):
        pass

    def display(self):
        print(self.__ans)


class CalcSum(Calculator):

    def calculate(self):
        self.ans = self.num1 + self.num2
        
class CalcDiff(Calculator):
        
    def calculate(self):
        self.ans = self.num1 - self.num2

class CalcProd(Calculator):
        
    def calculate(self):
        self.ans = self.num1 * self.num2

class CalcQuo(Calculator):
        
    def calculate(self):
        self.ans = self.num1 / self.num2



c = CalcSum(20,"3i4")
c.calculate()
c.display()

# c = CalcProd(20,12)
# c.calculate()
# c.display()