import numpy as np
import matplotlib.pyplot as plt

from Functions import F1, F2, F3
from NewtonMethod import NewtonMethod
from ChordMethod import ChordsMethod
from SimpleIterationsMethod import SimpleIterationsMethod
from SystemNewtonMethod import SystemNewtonMethod

def main():
    print("Введите номер функции, которую хотите решить:")
    print("1) F1(x) = x^3 - 3.125x^2 - 3.5x + 2.458")
    print("2) F2(x) = 2x^3 - 1.89x^2 - 5x + 2.34")
    print("3) F3(x) = e^x - 3")
    print("4) F4(x, y):")
    print("   x^2 + y^2 - 4 = 0")
    print("   -3 * x^2 + y = 0")
    function_choice = int(input())

    if function_choice not in range(1, 5):
        raise ValueError("Неверный выбор функции!")

    print("Выберите способ решения:")
    print("1) Метод Ньютона")
    print("2) Метод хорд")
    print("3) Метод простой итерации")
    print("4) Метод Ньютона для систем")
    choice_method = int(input())

    if choice_method not in range(1, 5):
        raise ValueError("Неверный выбор метода!")

    print("Как бы вы хотели получить значения границы интервала, "
          "начальное приближение к корню (в случае, где оно не высчитывается) и погрешность вычисления?")
    print("1 - вручную")
    print("2 - из файла")
    data_input = int(input())

    if data_input not in [1, 2]:
        raise ValueError("Неверный выбор способа получения данных!")

    segment = [0, 0]
    EPS = 0

    if data_input == 1:
        print("Введите границу отрезка через пробел:")
        segment[0], segment[1] = map(float, input().split())
        if segment[0] >= segment[1]:
            raise ValueError("Начальное значение интервала должно быть меньше конечного значения!")
        if (function_choice == 1 and F1(segment[0]) * F1(segment[1]) > 0) or \
                (function_choice == 2 and F2(segment[0]) * F2(segment[1]) > 0) or \
                (function_choice == 3 and F3(segment[0]) * F3(segment[1]) > 0):
            raise ValueError("На заданном интервале нет корня!")
        print("Введите погрешность:")
        EPS = float(input())
        if EPS < 0:
            raise ValueError("Некорректно введена погрешность!")
    elif data_input == 2:
        with open("test.txt", "r") as file:
            segment[0], segment[1], EPS = map(float, file.readline().split())

    if choice_method == 1:
        result = NewtonMethod.SolveEquation(segment, EPS, function_choice)
        print("Решение: x =", result)
    elif choice_method == 2:
        result = ChordsMethod.SolveEquation(segment, EPS, function_choice)
        print("Решение: x =", result)
    elif choice_method == 3:
        result = SimpleIterationsMethod.SolveEquation(segment, EPS, function_choice)
        print("Решение: x =", result)
    elif choice_method == 4:
        result = SystemNewtonMethod.SolveEquation(segment[0], segment[1], EPS)
        print("Приближенное решение: x =", result[0], ", y =", result[1])

if __name__ == "__main__":
    main()
