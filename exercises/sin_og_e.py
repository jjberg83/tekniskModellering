import numpy as np
import math
import matplotlib.pyplot as plt

class Function:
    def __init__(self, x, a = 10, b=1):
        self.x = x
        self.a = a
        self.b = b
        self.y = [0]*x

    def createArrayX(self):
        return np.arange(self.x)

    def createArrayY(self):
        for i in range(self.x):
            self.y[i] = self.a * np.sin(i) * (math.e)**(-self.b*i)
        return np.array(self.y)

    

enInstans = Function(10)
xEne = enInstans.createArrayX()
yEne = enInstans.createArrayY()
print(xEne)
print(yEne)
plt.plot(xEne, yEne)
plt.show()
# print(enArray)
# print(enInstans.a)
# print(enInstans.b)


