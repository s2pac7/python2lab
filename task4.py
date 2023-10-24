"""Напишите программу, демонстрирующую работу try\except\finally """

print("\t\tПодели первое число на второе")
try:
    number1 = int(input("1.Введите первое число "))
    number2 = int(input("2.Введите второе число "))

    result = number1 / number2

    print("Результат:", result)

except ZeroDivisionError:
    print("Нельзя делить на 0")
except ValueError:
    print("Некорректные данные")
else:
    print("Ошибок не было")
finally:
    print("Пока!")

