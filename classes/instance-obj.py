class x:
    counter = 1


while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


def f1(self, x, y):
    return min(x, x + y)
