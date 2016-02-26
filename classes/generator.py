def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in range(8, -1, -1):
    print(index)

print(sum(i * i for i in range(10)))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x * y for x, y in zip(xvec, yvec))

from math import pi, sin

sine_table = {x: sin(x * pi / 180) for x in range(0, 91)}
page = ('a', 'b', 'c')
unique_words = set(word for line in page for word in line.split())
print(unique_words)