import time
import numpy as np

try:
    start = time.time()
    N = int(input('Введите количество строк/столбцов матрицы > 3: '))
    while N < 4:
        N = int(input('Введите количество строк/столбцов матрицы > 3:'))
    K = int(input('Введите число К:'))
    A = np.random.randint(-10, 10, (N, N))        # задаем матрицу A
    F = np.copy(A)                                # задаем матрицу F
    time_next = time.time()
    print('Матрицa A:\n', A)
    a, b = 0, 0                       # переменная для подсчета количество нулей в C в нечетных столбцах
    for i in range(N):
        for j in range(N):
            if i < (N // 2) and j > (N // 2 - (N - 1) % 2):
                if j % 2 == 0 and A[i][j] == 0:
                    a += 1
                if i == 0 or i == (N // 2 - 1) or j == (N // 2 + N % 2) or j == (N - 1):
                    b += int(A[i][j])
    print(a, b,)
    if a > b:
        for i in range(N // 2):       # если нулей больше то поменять местами B и C симметрично
            F[i] = F[i][::-1]
    else:                             # иначе B и Е поменять местами несимметрично
        for i in range(N // 2):
            for j in range(N // 2):
                F[i][j], F[i + N // 2 + N % 2][j + N // 2 + N % 2] = F[i + N // 2 + N % 2][j + N // 2 + N % 2], F[i][j]
    print('Матрицa F:',F)

    if np.linalg.det(A) > sum(np.diagonal(F)):
        if np.linalg.det(A) == 0:
            print("Матрица А вырожденная, дальнейшие вычисления невозможны")
        else:
            print(f"(A^(-1)A^T–KF^(-1))\n{((np.dot(np.linalg.matrix_power(A, -1), np.transpose(A))) - (np.dot(K, np.linalg.matrix_power(F, -1))))}")
    else:
        if np.linalg.det(F) == 0 or np.linalg.det(np.tril(A)) == 0:
            print("Матрица F или G вырожденная, дальнейшие вычисления невозможны")
        else:
            print (f'Нижняя Треугольная Матрица G:\n{np.tril(A)}')
            print(f"A+G^(-1)-F^(-1))*K\n{(A + np.linalg.inv(np.tril(A)) - np.linalg.inv(F)) * K}")
    print(f"Programm time: {time.time()-start}")
except ValueError:
    print("Введённые данные не число, перезапустите программу!")