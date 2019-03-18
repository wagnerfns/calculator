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
    def setAddition(self):
        return(self.value1 + self.value2)

    def setSubtraction(self):
        return(self.value1 - self.value2)

    def setMultiplication(self):
        return(self.value1 * self.value2)

    def setDivision(self):
        if(self.value2 != 0):
            return(self.value1 / self.value2)
        else:
            print("result: division by zero")
            return(None) 
    def setRoot(self):
        return(math.sqrt(self.value1))

    def setPotentiation(self):
        return(self.value1 ** 2)

    def avg(self):
        return(float(sum(self.value1))/len(self.value1))
