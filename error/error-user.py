class MyError(Exception):
    def __int__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print('My Exception occurred,value:', e.value)

    # raise MyError('Oops')
