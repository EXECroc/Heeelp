import numpy as np

def generate_matrix(rows, cols):
    return np.random.randint(1, 10, (rows, cols))

def add_matrices(a, b):
    if a.shape != b.shape:
        raise ValueError("Матрицы должны быть одинакового размера")
    return a + b

def multiply_matrices(a, b):
    if a.shape[1] != b.shape[0]:
        raise ValueError("Число столбцов первой матрицы должно совпадать с числом строк второй")
    return np.dot(a, b)

def transpose_matrix(a):
    return a.T

# Пример использования
A = generate_matrix(3, 3)
B = generate_matrix(3, 3)
C = generate_matrix(3, 2)
D = generate_matrix(2, 3)

print("Матрица A:")
print(A)
print("Матрица B:")
print(B)
print("Сумма A + B:")
print(add_matrices(A, B))
print("Произведение A * D:")
print(multiply_matrices(A, D))
print("Транспонированная A:")
print(transpose_matrix(A))
