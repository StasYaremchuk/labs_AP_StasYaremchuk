def XO(x):
    count_x = 0
    count_o = 0
    for i in x:
        if i == 'x' or i == 'X':
            count_x += 1
        elif i == 'o' or i == 'O' or i == '0':
            count_o += 1
    if count_x == 0 and count_o == 0:
        return False
    return count_x == count_o, count_x, count_o


print("")
while True:
    res = input("Введіть стрічку: ")
    if res == 'exit':
        print("Кінець")
        break

    result, count_x, count_o = XO(res)
    if result == False:
        print(f"У Вас не одинкова кількість \"X\" і \"O\", \nRількість 'x': {count_x}, кількість 'o': {count_o}")
        print("Щоб вийти напишіть 'exit'\n")
    elif result == True:
        print(f"Так, кількість 'x': {count_x}, \nКількість 'o': {count_o}")
        print("Щоб вийти напишіть 'exit'\n")
