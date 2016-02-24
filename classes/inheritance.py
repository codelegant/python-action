class Bag:
    def __init__(self, x):
        self.data = []
        self.x = x

    def add(self, x):
        self.data.append(x)

    def getvalue(self):
        return self.data


class Bag2:
    def __init__(self, x):
        self.data = []
        self.x = x

    def showname(self):
        print(self.data)

    def printx(self):
        print(self.x)


# 多继承的两个类的参数必须一致
class SubBag(Bag, Bag2):
    def addthrice(self, x):
        self.add(x)
        self.add(x)
        self.add(x)


m = SubBag(10)
m.addthrice(3)
print(m.getvalue())
m.showname()
m.printx()
