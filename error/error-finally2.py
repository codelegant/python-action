def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Result is', result)
    finally:
        print('executing finally clause')


divide(2, 0)
