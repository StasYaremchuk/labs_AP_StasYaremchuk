a = 0.5
b = 1
h = 0.05  # крок
d = 0.001  # похибка
r = round


def fun1(x):
    sum = 0
    k = 1
    while True:
        k += 1
        vuraz1 = (x + 2) / (k * (k + 2))
        sum += vuraz1
        if vuraz1 < d:
            break
    return sum


x = a
while x <= b:
    print(x, "\t -->\t", r(fun1(x), 3))
    x += h
    x = round(x, 3)
