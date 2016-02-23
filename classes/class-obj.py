class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'Hello World'


print(MyClass.i)
print(MyClass.f(MyClass))
print(MyClass.__doc__)
x = MyClass()
print(x.f())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


y = Complex(3.0, -45)
print(y.r), print(y.i)
