"""Напишите функцию solve(a, b, c), которая принимает в
качестве аргументов три целых числа a, b, c – коэффициенты квадратного
уравнения ax2+bx+c= и возвращает его корни в порядке возрастания"""

from math import sqrt
def solve(a, b, c):
    D = b ** 2 - 4*a*c
    if D > 0:
        x_1 = (-b - sqrt(D)) / 2 * a
        x_2 = (-b + sqrt(D)) / 2 * a
        print(f"2 корня:\nx1 = {x_1}\nx2 = {x_2}")
    elif D == 0:
        x = (-b) / 2 * a
        print(f"1 корень:\nx = {x}")
    else:
        print("Корней нет")


print("\t\t\tax^2+bx+c")
print("Пусть а, b, c - целые числа")
try:
    a = int(input("Введите коэффицент a: "))
    b = int(input("Введите коэффицент b: "))
    c = int(input("Введите коэффицент c: "))
except ValueError:
    print("Вы ввели некорректные данные")
except InterruptedError:
    print("Вы ввели не целые числа")
else:
    solve(a, b, c)

