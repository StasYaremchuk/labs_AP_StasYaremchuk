import math

question = int(input("Ведіть, який приклад хочете розвязати від 1 до 8: "))

if question == 1:
    x = 2.632
    y = 0.731
    rslt1 = math.sin(x ** 2) + math.cos(2 * x + y) - 14 * pow(pow(x, 2) + y, 3)
    print(rslt1)
elif question == 2:
    x = 3.142
    z = 0.543
    rslt2 = math.tan(x ** 0.5) + 165 * z ** 6 + (x ** 2 - z) ** 0.25
    print(rslt2)
elif question == 3:
    x = 4.112
    y = 1.628
    rslt3 = (3 * x ** 2 + 1) / (5 * y) + (2 * math.tan(x + 1)) / (y - 2)
    print(rslt3)
elif question == 4:
    x = 2.361
    y = 1.149
    rslt4 = 13 * x * y + math.log(x / y, math.e) - 17 * math.sin(x ** 2 - y)
    print(rslt4)
elif question == 5:
    x = 2.735
    z = 7.218
    rslt5 = pow((z + x) / math.cos(x) + (math.sin(x) * math.cos(x)) ** 0.5, 2) + 16 * z
    print(rslt5)
elif question == 6:
    y = 6.153
    z = 1.001
    rslt6 = math.tan(math.cos(z)) + (4 * math.sin(z)) / math.cos(y) + (y * z) ** 0.5
    print(rslt6)
elif question == 7:
    x = 12.394
    y = 7.139
    rslt7 = math.tan(x) ** 0.5 + pow(x + y, math.log(x, math.e))
    print(rslt7)
elif question == 8:
    z = 9.761
    rslt8 = z ** 6 + 13 * (z ** 4) + 7 * (z ** 3) + 14 * (z ** 2) - 2 * z + 21
    print(rslt8)
else:
    print("Ви написали, щось не вірно")
