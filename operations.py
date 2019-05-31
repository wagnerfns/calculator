import math

class Operations:
    def __init__(self, value1):
        self.value1 = value1

    def __init__(self, value1, value2, verbose=True):
        if(verbose):
            self.value1 = value1
            self.value2 = value2
        else:
            self.value1 = value1

    def addition(self):
        return(self.value1 + self.value2)

    def subtraction(self):
        return(self.value1 - self.value2)

    def multiplication(self):
        return(self.value1 * self.value2)

    def division(self):
        if(self.value2 != 0):
            return(self.value1 / self.value2)
        else:
            print("result: division by zero")
            return(None)

    def root(self):
        return(math.sqrt(self.value1))

    def potentiation(self):
        return(self.value1 ** 2)

    def avg(self):
        return float(sum(self.value1) / len(self.value1))

    def factorial(self):
        return math.factorial(self.value1)
