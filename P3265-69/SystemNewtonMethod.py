from Functions import F4, F5, DF4_DX, DF4_DY, DF5_DX, DF5_DY
import numpy as np

class SystemNewtonMethod:
    @staticmethod
    def SolveEquation(x0, y0, eps):
        x = x0
        y = y0
        iterations = 0
        errors = []

        dx = (-F4(x, y) * DF5_DY() + F5(x, y) * DF4_DY(y)) / (DF4_DX(x) * DF5_DY() - DF5_DX(x) * DF4_DY(y))
        dy = (-F5(x, y) * DF4_DX(x) + F4(x, y) * DF5_DX(x)) / (DF4_DX(x) * DF5_DY() - DF5_DX(x) * DF4_DY(y))
        x += dx
        y += dy
        iterations += 1

        while abs(dx) > eps and abs(dy) > eps:
            dx = (-F4(x, y) * DF5_DY() + F5(x, y) * DF4_DY(y)) / (DF4_DX(x) * DF5_DY() - DF5_DX(x) * DF4_DY(y))
            dy = (-F5(x, y) * DF4_DX(x) + F4(x, y) * DF5_DX(x)) / (DF4_DX(x) * DF5_DY() - DF5_DX(x) * DF4_DY(y))
            x += dx
            y += dy
            iterations += 1
            errors.append(np.sqrt(dx * dx + dy * dy))

        print("Количество итераций:", iterations)
        print("Вектор погрешностей:", errors)

        result = [x, y]
        return result
