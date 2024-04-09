class SimpleIterationsMethod:
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

        def df1(x):
            # Implementation of derivative of function F1
            pass

        def df2(x):
            # Implementation of derivative of function F2
            pass

        def df3(x):
            # Implementation of derivative of function F3
            pass

        functions = {1: (f1, df1), 2: (f2, df2), 3: (f3, df3)}

        lambda_val = -1 / max(functions[function_choice][1](segment[0]), functions[function_choice][1](segment[1]))

        if 1 + lambda_val * functions[function_choice][1](segment[0]) > 1 or \
                1 + lambda_val * functions[function_choice][1](segment[1]) > 1:
            raise RuntimeError("Условие сходимости не выполняется.")

        x0 = segment[0]
        counter = 0

        while True:
            x = x0 + lambda_val * functions[function_choice][0](x0)
            counter += 1

            if abs(x - x0) < eps:
                print("Корень уравнения:", x)
                print("Значение функции в х:", functions[function_choice][0](x))
                print("Количество итераций:", counter)
                return x

            x0 = x

        raise ValueError("Невозможно посчитать начальное приближение!")
