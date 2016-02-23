class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

    def getvalue(self):
        return self.data


class SubBag(Bag):
    def addthrice(self, x):
        self.add(x)
        self.add(x)
        self.add(x)


m = SubBag()
m.addthrice(3)
print(m.getvalue())
