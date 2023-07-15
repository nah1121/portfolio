def input_matrix():
    rows = []
    print("Enter the matrix row by row (space separated values):")
    while True:
        row = input()
        if not row:
            break
        rows.append(list(map(float, row.split())))
    return rows


def get_matrix_dimensions(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    return num_rows, num_cols


def add_matrices(matrix1, matrix2):
    if get_matrix_dimensions(matrix1) != get_matrix_dimensions(matrix2):
        print("Error: Matrix sizes don't match!")
        return None
    result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(get_matrix_dimensions(matrix1)[1])] for i in
                     range(get_matrix_dimensions(matrix1)[0])]
    return result_matrix


def subtract_matrices(matrix1, matrix2):
    if get_matrix_dimensions(matrix1) != get_matrix_dimensions(matrix2):
        print("Error: Matrix sizes don't match!")
        return None
    result_matrix = [[matrix1[i][j] - matrix2[i][j] for j in range(get_matrix_dimensions(matrix1)[1])] for i in
                     range(get_matrix_dimensions(matrix1)[0])]
    return result_matrix


def multiply_matrices(matrix1, matrix2):
    if get_matrix_dimensions(matrix1)[1] != get_matrix_dimensions(matrix2)[0]:
        print("Error: Matrix sizes don't match!")
        return None
    result_matrix = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(get_matrix_dimensions(matrix2)[0])) for j in
                      range(get_matrix_dimensions(matrix2)[1])] for i in range(get_matrix_dimensions(matrix1)[0])]
    return result_matrix


def transpose_matrix(matrix):
    result_matrix = [[matrix[j][i] for j in range(get_matrix_dimensions(matrix)[0])] for i in
                     range(get_matrix_dimensions(matrix)[1])]
    return result_matrix


def get_matrix_minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def get_matrix_determinant(matrix):
    """
    Calculates the determinant of a square matrix recursively.
    :param matrix: a square matrix
    :return: the determinant of the matrix
    """
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(len(matrix)):
            sub_matrix = []
            for i in range(1, len(matrix)):
                row = []
                for k in range(len(matrix)):
                    if k != j:
                        row.append(matrix[i][k])
                sub_matrix.append(row)
            determinant += (-1) ** j * matrix[0][j] * get_matrix_determinant(sub_matrix)
        return determinant


def get_matrix_inverse(matrix):
    # Check if matrix is square
    if len(matrix) != len(matrix[0]):
        print("Error: Matrix is not square.")
        return None

    # Create augmented matrix [A | I]
    n = len(matrix)
    aug_matrix = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    # Perform row operations to transform [A | I] into [I | A^-1]
    for i in range(n):
        # If diagonal element is zero, swap with a row below that has a nonzero diagonal element
        if aug_matrix[i][i] == 0:
            for j in range(i + 1, n):
                if aug_matrix[j][i] != 0:
                    aug_matrix[i], aug_matrix[j] = aug_matrix[j], aug_matrix[i]
                    break
            else:
                print("Error: Matrix is singular.")
                return None

        # Divide entire row by diagonal element
        diagonal = aug_matrix[i][i]
        for j in range(n * 2):
            aug_matrix[i][j] /= diagonal

        # Perform row operations to set all elements below diagonal to zero
        for j in range(i + 1, n):
            factor = aug_matrix[j][i]
            for k in range(n * 2):
                aug_matrix[j][k] -= factor * aug_matrix[i][k]

    # Perform row operations to set all elements above diagonal to zero
    for i in range(n - 1, -1, -1):
        for j in range(i):
            factor = aug_matrix[j][i]
            for k in range(n * 2):
                aug_matrix[j][k] -= factor * aug_matrix[i][k]

    # Extract inverse matrix from augmented matrix
    inv_matrix = [row[n:] for row in aug_matrix]

    return inv_matrix


def operate_matrices(matrix1, matrix2, operator):
    if operator == '+':
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            print("Error: Matrices must be of same size.")
            return None
        else:
            result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in
                             range(len(matrix1))]
            return result_matrix
    elif operator == '-':
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            print("Error: Matrices must be of same size.")
            return None
        else:
            result_matrix = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in
                             range(len(matrix1))]
            return result_matrix
    elif operator == '*':
        if len(matrix1[0]) != len(matrix2):
            print("Error: Number of columns in first matrix must match number of rows in second matrix.")
            return None
        else:
            result_matrix = [
                [sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i
                in range(len(matrix1))]
            return result_matrix
    elif operator == 't' or operator == 'T':
        result = transpose_matrix(matrix1)
        return result
    elif operator == 'det':
        if len(matrix1) != len(matrix1[0]):
            print("Error: Matrix must be square.")
            return None
        else:
            result = get_matrix_determinant(matrix1)
            return result
    elif operator == 'inv':
        if len(matrix1) != len(matrix1[0]):
            print("Error: Matrix must be square.")
            return None
        else:
            result_matrix = get_matrix_inverse(matrix1)
            return result_matrix
    else:
        print("Error: Invalid operator.")
        return None


def print_matrix(matrix):
    if isinstance(matrix, float):
        print(matrix)
    else:
        for row in matrix:
            for element in row:
                print(element, end=' ')
            print()



print("Enter the first matrix:")
matrix1 = input_matrix()
print("Addition  +""\n"
      "Subtraction  -""\n"
      "Multiplication  *""\n"
      "Transpose  T""\n"
      "Determinant  det""\n"
      "Inverse  inv")
print("Select an operation (+, -, *, T, det, inv):")
operator = input()

if operator in ["+", "-", "*"]:
    print("Enter the second matrix:")
    matrix2 = input_matrix()
else:
    matrix2 = None

result_matrix = operate_matrices(matrix1, matrix2, operator)

if result_matrix is not None:
    print("Result:")
    print_matrix(result_matrix)
