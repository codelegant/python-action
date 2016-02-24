class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def getvalue(self):
        return self.data


class Bag2:
    def __init__(self):
        self.data = []

    def showname(self):
        print(self.data)


class SubBag(Bag, Bag2):
    def addthrice(self, x):
        self.add(x)
        self.add(x)
        self.add(x)


m = SubBag()
m.addthrice(3)
print(m.getvalue())
m.showname()
