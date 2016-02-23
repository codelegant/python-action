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


bag = Bag()
bag.add(4)
bag.addtwice(5)
print(bag.getvalue())
print(bag.__class__)
print(isinstance(bag, Bag))
