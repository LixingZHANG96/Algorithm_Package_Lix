import numpy as np


def square_matrix_multiplication(A, B):
    """The main function for recursive square matrix multiplication."""
    A = np.array(A)
    B = np.array(B)
    n = A.shape[0]
    if n == 1:
        C = A * B
    else:
        A11, A12, A21, A22 = matrix_partition(A)
        B11, B12, B21, B22 = matrix_partition(B)
        C11 = square_matrix_multiplication(A11, B11) + \
            square_matrix_multiplication(A12, B21)
        C12 = square_matrix_multiplication(A11, B12) + \
            square_matrix_multiplication(A12, B22)
        C21 = square_matrix_multiplication(A21, B11) + \
            square_matrix_multiplication(A22, B21)
        C22 = square_matrix_multiplication(A21, B12) + \
            square_matrix_multiplication(A22, B22)
        C = matrices_combination(C11, C12, C21, C22)
        print("The output submatrix for this round:\n", C)

    return C


def matrix_partition(C):
    row_middle = int(np.floor(C.shape[0]/2))
    col_middle = int(np.floor(C.shape[1]/2))
    C11 = C[:row_middle, :col_middle]
    C12 = C[:row_middle, col_middle:]
    C21 = C[row_middle:, :col_middle]
    C22 = C[row_middle:, col_middle:]

    return C11, C12, C21, C22


def matrices_combination(C11, C12, C21, C22):
    return np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))


if __name__ == '__main__':
    A = np.random.randint(0, 10, (8, 8))
    B = np.random.randint(0, 10, (8, 8))
    print("Input Matrix A:\n", A)
    print("Input Matrix B:\n", B)
    C = square_matrix_multiplication(A, B)
    print("A * B =\t", C)
