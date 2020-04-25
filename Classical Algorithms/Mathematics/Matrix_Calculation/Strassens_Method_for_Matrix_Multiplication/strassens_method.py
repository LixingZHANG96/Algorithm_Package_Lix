import numpy as np


def strassens_method(A, B):
    """The main function for recursive square matrix multiplication."""
    A = np.array(A)
    B = np.array(B)
    n = A.shape[0]
    if n == 1:
        C = A * B
    else:
        A11, A12, A21, A22 = matrix_partition(A)
        B11, B12, B21, B22 = matrix_partition(B)

        S1 = B12 - B22
        S2 = A11 + A12
        S3 = A21 + A22
        S4 = B21 - B11
        S5 = A11 + A22
        S6 = B11 + B22
        S7 = A12 - A22
        S8 = B21 + B22
        S9 = A11 - A21
        S10 = B11 + B12

        P1 = strassens_method(A11, S1)
        P2 = strassens_method(S2, B22)
        P3 = strassens_method(S3, B11)
        P4 = strassens_method(A22, S4)
        P5 = strassens_method(S5, S6)
        P6 = strassens_method(S7, S8)
        P7 = strassens_method(S9, S10)

        C11 = P5 + P4 - P2 + P6
        C12 = P1 + P2
        C21 = P3 + P4
        C22 = P5 + P1 - P3 - P7
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
    C = strassens_method(A, B)
    print("A * B =\n", C)
