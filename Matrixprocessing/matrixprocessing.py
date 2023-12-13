def read_matrix():
    # Зчитує матрицю з введення користувача
    rows, cols = map(int, input().split())
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    # Виводить матрицю на екран
    for row in matrix:
        print(*row)

def add_matrices(matrix1, matrix2):
    # Додає дві матриці, якщо вони мають однаковий розмір
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("ERROR")
        return

    result = []
    for i in range(len(matrix1)):
        row = [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        result.append(row)

    for row in result:
        print(*row)

def multiply_by_constant(matrix, constant):
    # Множить матрицю на константу
    result = [[element * constant for element in row] for row in matrix]

    for row in result:
        print(*row)

def multiply_matrices(matrix1, matrix2):
    # Множить дві матриці
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            value = 0
            for k in range(len(matrix2)):
                value += matrix1[i][k] * matrix2[k][j]
            row.append(value)
        result.append(row)

    for row in result:
        print(*row)

def transpose_matrix(matrix, transpose_type):
    # Транспонує матрицю залежно від обраного типу транспонування
    if transpose_type == 1:  # Main diagonal
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif transpose_type == 2:  # Side diagonal
        result = [[matrix[len(matrix) - 1 - j][len(matrix[0]) - 1 - i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    elif transpose_type == 3:  # Vertical line
        result = [row[::-1] for row in matrix]
    elif transpose_type == 4:  # Horizontal line
        result = matrix[::-1]
    else:
        print("Invalid transpose type.")
        return

    for row in result:
        print(*row)

def determinant(matrix):
    # Обчислює визначник матриці
    n = len(matrix)
    if n != len(matrix[0]):
        print("Matrix is not square. Determinant is undefined.")
        return None

    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            cofactor = matrix[0][i] * determinant(get_minor(matrix, 0, i))
            det += ((-1) ** i) * cofactor
        return det

def get_minor(matrix, row, col):
    # Повертає мінор матриці
    return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]

def inverse_matrix(matrix):
    # Знаходження зворотної матриці методом Гаусса-Жордана
    n = len(matrix)
    augmented_matrix = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    for i in range(n):
        # Нормалізація поточного рядка
        max_row = max(range(i, n), key=lambda j: abs(augmented_matrix[j][i]))
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]

        # Обнулення інших рядків у стовпці
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i] / augmented_matrix[i][i]
                augmented_matrix[j] = [x - factor * y for x, y in zip(augmented_matrix[j], augmented_matrix[i])]

    # Нормалізація діагоналі до одиниць
    for i in range(n):
        factor = 1 / augmented_matrix[i][i]
        augmented_matrix[i] = [x * factor for x in augmented_matrix[i]]

    # Вилучення оригінальної матриці
    inverse = [row[n:] for row in augmented_matrix]

    return inverse

def menu():
    # Виводить меню користувачеві
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            print("Enter size of first matrix:")
            matrix_A = read_matrix()

            print("Enter first matrix:")
            print_matrix(matrix_A)

            print("Enter size of second matrix:")
            matrix_B = read_matrix()

            print("Enter second matrix:")
            print_matrix(matrix_B)

            print("The result is:")
            add_matrices(matrix_A, matrix_B)
        elif choice == "2":
            print("Enter size of matrix:")
            matrix_C = read_matrix()

            constant = float(input("Enter constant: "))
            print("The result is:")
            multiply_by_constant(matrix_C, constant)
        elif choice == "3":
            print("Enter size of first matrix:")
            matrix_D = read_matrix()

            print("Enter first matrix:")
            print_matrix(matrix_D)

            print("Enter size of second matrix:")
            matrix_E = read_matrix()

            print("Enter second matrix:")
            print_matrix(matrix_E)

            print("The result is:")
            multiply_matrices(matrix_D, matrix_E)
        elif choice == "4":
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")

            transpose_type = int(input("Your choice: "))
            print("Enter matrix size:")
            matrix_F = read_matrix()

            print("Enter matrix:")
            print_matrix(matrix_F)

            print("The result is:")
            transpose_matrix(matrix_F, transpose_type)
        elif choice == "5":
            print("Enter matrix size:")
            matrix_G = read_matrix()

            print("Enter matrix:")
            print_matrix(matrix_G)

            det = determinant(matrix_G)
            if det is not None:
                print("The result is:", det)
        elif choice == "6":
            print("Enter matrix size:")
            matrix_H = read_matrix()

            print("Enter matrix:")
            print_matrix(matrix_H)

            det = determinant(matrix_H)
            if det == 0:
                print("This matrix doesn't have an inverse.")
            else:
                inverse = inverse_matrix(matrix_H)
                print("The result is:")
                print_matrix(inverse)
        else:
            print("Invalid choice. Please enter a valid option.")
