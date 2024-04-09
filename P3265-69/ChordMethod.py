class ChordsMethod:
    @staticmethod
    def find_root(segment, function_choice):
        def f1(x):
            # Implementation of function F1
            pass

        def f2(x):
            # Implementation of function F2
            pass

        def f3(x):
            # Implementation of function F3
            pass

        if function_choice == 1:
            fa = f1(segment[0])
            fb = f1(segment[1])
        elif function_choice == 2:
            fa = f2(segment[0])
            fb = f2(segment[1])
        elif function_choice == 3:
            fa = f3(segment[0])
            fb = f3(segment[1])
        else:
            raise ValueError("Невозможно посчитать начальное приближение!")

        if fa * fb > 0:
            raise ValueError("Начальные точки на отрезке не обеспечивают смены знака функции!")

        return segment[0] - ((segment[1] - segment[0]) * fa / (fb - fa))

    @staticmethod
    def solve_equation(segment, eps, function_choice):
        def f1(x):
            # Implementation of function F1
            pass

        def f2(x):
            # Implementation of function F2
            pass

        def f3(x):
            # Implementation of function F3
            pass

        x = ChordsMethod.find_root(segment, function_choice)
        counter = 0

        while True:
            if function_choice == 1:
                if abs(f1(x)) > eps:
                    if f1(segment[0]) * f1(x) < 0:
                        segment[1] = x
                    elif f1(segment[1]) * f1(x) < 0:
                        segment[0] = x
                    x = ChordsMethod.find_root(segment, function_choice)
                    counter += 1
                else:
                    break
            elif function_choice == 2:
                if abs(f2(x)) > eps:
                    if f2(segment[0]) * f2(x) < 0:
                        segment[1] = x
                    elif f2(segment[1]) * f2(x) < 0:
                        segment[0] = x
                    x = ChordsMethod.find_root(segment, function_choice)
                    counter += 1
                else:
                    break
            elif function_choice == 3:
                if abs(f3(x)) > eps:
                    if f3(segment[0]) * f3(x) < 0:
                        segment[1] = x
                    elif f3(segment[1]) * f3(x) < 0:
                        segment[0] = x
                    x = ChordsMethod.find_root(segment, function_choice)
                    counter += 1
                else:
                    break

        print("Полученное значение x:", x)
        print("Количество итераций:", counter)

        if function_choice == 1:
            print("Значение функции в х:", f1(x))
        elif function_choice == 2:
            print("Значение функции в х:", f2(x))
        elif function_choice == 3:
            print("Значение функции в х:", f3(x))

        return x
