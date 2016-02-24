s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))


class Reverse:
    """添加迭代器"""

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        data = self.data[self.index]
        self.index = self.index + 1
        return data


rev = Reverse('laichuanfeng')
for char in rev:
    print(char)
