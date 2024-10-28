from math import cos, tan, atan

a = 0.5
b = 0.9
h = 0.02
r = round


def res(x):
    if x < 0.6:
        return cos(x ** 0.5)
    elif 0.6 <= x < 0.7:
        return 1 / tan(x ** 2)
    elif x >= 0.7:
        return atan(x ** 3)


x = a
print("Функція на проміжку [0.5, 0.9] з кроком 0.02:")
while x <= b:
    print(x, "\t -->\t", r(res(x), 3))
    x += h
    x = round(x, 3)
