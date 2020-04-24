## Square Matrix Multiplication Recuresive
### 1. Problem Set-up

- Description: Using the direct method, the matrix multiplication takes a time complexity of Θ(n^3). However, with the recuresive multiplication algorithm described here, the time complexity would be Θ(n^2).

 To solve the general matrix multiplication porblem however, another 2 algorithms for row/column-array multiplication must be defined. For this problem alone, Only n = 2^k(k=0,1,2...) are allowed.

- Input: 2 square matrices A and B of the same size n x n.

- Output: The matrix-wise multiplication C of A and B with size n x n.

### 2. Pseudocode
```
SQUARE-MATRIX-MULTIPLICATION(A, B)
  n = A.rows
  if n == 1 then:
    C = A * B
  else:
    A11, A12, A21, A22 = MATRIX-PARTITION(A)
    B11, B12, B21, B22 = MATRIX-PARTITION(B)
    C11 = SQUARE-MATRIX-MULTIPLICATION(A11, B11) + SQUARE-MATRIX-MULTIPLICATION(A12, B21)
    C12 = SQUARE-MATRIX-MULTIPLICATION(A11, B12) + SQUARE-MATRIX-MULTIPLICATION(A12, B22)
    C21 = SQUARE-MATRIX-MULTIPLICATION(A21, B11) + SQUARE-MATRIX-MULTIPLICATION(A22, B21)
    C11 = SQUARE-MATRIX-MULTIPLICATION(A21, B12) + SQUARE-MATRIX-MULTIPLICATION(A22, B22)
    C = MATRIX-COMBINATION(C11, C12, C21, C22)
  return C
```
```
MATRIX-PARTITION(C)
  r = C.rows
  c = C.columns
  r_middle = floor(r/2)
  c_middle = floor(c/2)
  C11 = C[1:r_middle, 1:c_middle]
  C12 = C[1:r_middle, c_middle:c]
  C21 = C[r_middle:r, 1:c_middle]
  C11 = C[r_middle:r, c_middle:c]
  return C11, C12, C21, C22
```
```
MATRIX-COMBINATION(C11, C12, C21, C22)
  C1 = stack_up_horizontally(C11, C12)
  C2 = stack_up_horizontally(C21, C22)
  C = stack_up_vertically(C1, C2)
  return C
```
### 3. Algorithm Analysis
