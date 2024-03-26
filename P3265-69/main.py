import numpy as np

E = 0.0001

def calculate_determinant(matrix, n):
    det = 1.0

    if n == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    if n == 3:
        det = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] + matrix[0][2] * matrix[1][0] * matrix[2][1] - matrix[0][2] * matrix[1][1] * matrix[2][0] - matrix[0][0] * matrix[1][2] * matrix[2][1] - matrix[0][1] * matrix[1][0] * matrix[2][2]
        return det

    for i in range(n):
        pivot = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[pivot][i]):
                pivot = j
        if pivot != i:
            det *= -1.0
            matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
        det *= matrix[i][i]
        if abs(det) < E:
            return 0.0
        for j in range(i + 1, n):
            coefficient = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= coefficient * matrix[i][k]
    return det

def gauss_solve(matrix, y_values, n):
    answers = [0] * n
    k, index = 0, 0
    for k in range(n):
        max_val = abs(matrix[k][k])
        index = k
        for i in range(k + 1, n):
            if abs(matrix[i][k]) > max_val:
                max_val = abs(matrix[i][k])
                index = i

        matrix[k], matrix[index] = matrix[index], matrix[k]
        y_values[k], y_values[index] = y_values[index], y_values[k]

        for i in range(k, n):
            temp = matrix[i][k]
            if abs(temp) < E:
                continue
            for j in range(k, n):
                matrix[i][j] = matrix[i][j] / temp
            y_values[i] = y_values[i] / temp
            if i == k:
                continue
            for j in range(n):
                matrix[i][j] = matrix[i][j] - matrix[k][j]
            y_values[i] = y_values[i] - y_values[k]

    for k in range(n - 1, -1, -1):
        answers[k] = y_values[k]
        for i in range(k):
            y_values[i] = y_values[i] - matrix[i][k] * answers[k]
    return answers


def print_matrix(matrix_a, vector_b, n):
    print("Треугольная матрица: ")
    for i in range(n):
        for j in range(n):
            print(matrix_a[i][j], end="\t")
        print("|", vector_b[i])

def print_results(vector_x, residuals):
    print("Вектор неизвестных равны: ")
    for i in range(len(vector_x)):
        print(f"x[{i}] = {vector_x[i]}")
    print("Вектор невязок равны: ")
    for i in range(len(residuals)):
        print(f"r[{i}] = {residuals[i]}")

if __name__ == "__main__":
    n = int(input("Введите количество уравнений: "))
    if n > 20:
        print("Количество уравнений превышает допустмиое :(")
        exit()

    matrix_a = np.zeros((n, n))
    vector_y = np.zeros(n)

    print("Каким способом хотите заполнить матрицу?")
    print("1 - С помощью файла")
    print("2 - Вручную")
    choice = int(input())
    if choice == 1:
        filename = input("Введите имя файла: ")
        try:
            with open(filename, 'r') as file:
                for i in range(n):
                    matrix_a[i] = list(map(float, file.readline().split()))
                vector_y = list(map(float, file.readline().split()))
        except IOError:
            print("Ошибка чтения файла")
            exit()
    else:
        for i in range(n):
            print(f"Введите коэффициенты {i + 1}-го уравнения через пробел: ")
            matrix_a[i] = list(map(float, input().split()))
        print("Введите правые части уравнений через пробел ")
        vector_y = list(map(float, input().split()))

    print_matrix(matrix_a, vector_y, n)
    det = np.linalg.det(matrix_a)
    print("Определитель матрицы равен: ", det)
    if det != 0.0:
        vector_x = np.linalg.solve(matrix_a, vector_y)
        residuals = np.dot(matrix_a, vector_x) - vector_y
        print_results(vector_x, residuals)
    else:
        print("Определитель матрицы равен 0 => система либо имеет бесконечное множество решений, либо не имеет решений, т. е. несовместна")


