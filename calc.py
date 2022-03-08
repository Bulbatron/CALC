# в папке dist exe файл калькулятора
from num2words import num2words

print("Целочисленный калькулятор")
znak = input("для продолжения введите любое значение, либо 0 для выхода")
while znak != '0':
    what = input("введите математическую операцию ('+', '-', '*', '/' ):")
    if what in ('+', '-', '*', '/'):
        a = int(input("введите первое значение:"))
        b = int(input("введите второе значение:"))
    if what == "+":
        c = a + b
        print("Сумма равна:" + num2words(c, lang='ru'))
    elif what == "-":
        c = a - b
        print("Разность равна: " + num2words(c, lang='ru'))
    elif what == "*":
        c = a * b
        print("Произведение равно: " + num2words(c, lang='ru'))
    elif what == "/":
        if a != 0:
            c = a / b
            print("Частное равно: " + + num2words(c, lang='ru'))
        else:
            print("Делить на нуль нельзя!")
    elif what == "0":
        break
    else:
        print("Введите корректную математическую операцию!")
    if znak == "0":
        break
print("калькулятор остановлен")
