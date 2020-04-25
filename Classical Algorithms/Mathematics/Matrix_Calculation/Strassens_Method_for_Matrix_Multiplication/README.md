## Matrix Multiplication Strassen's Method
### 1. Problem Set-up

- Description: Using the recuresive multiplication algorithm, the time complexity is `$\Theta(n^2)$`. The Strassen's method to be described here takes a step even further and reduces the time complexity to `$\Theta(n^{lg7})$`

    As described before, for this problem alone, Only `$n = 2^k(k=0,1,2...)$` are allowed.

- Input: 2 square matrices A and B of the same size `$n \times n$`.

- Output: The matrix-wise multiplication C of A and B with size `$n \times n$`.

### 2. Pseudocode
```pseudocode
STRASSENs-METHOD(A, B)
  n = A.rows
  if n == 1 then:
    C = A * B
  else:
    A11, A12, A21, A22 = MATRIX-PARTITION(A)
    B11, B12, B21, B22 = MATRIX-PARTITION(B)

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

    P1 = STRASSENs-METHOD(A11, S1)
    P2 = STRASSENs-METHOD(S2, B22)
    P3 = STRASSENs-METHOD(S3, B11)
    P4 = STRASSENs-METHOD(A22, S4)
    P5 = STRASSENs-METHOD(S5, S6)
    P6 = STRASSENs-METHOD(S7, S8)
    P7 = STRASSENs-METHOD(S9, S10)

    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 -P7

    C = MATRIX-COMBINATION(C11, C12, C21, C22)
  return C
```

```pseudocode
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

```pseudocode
MATRIX-COMBINATION(C11, C12, C21, C22)
  C1 = stack_up_horizontally(C11, C12)
  C2 = stack_up_horizontally(C21, C22)
  C = stack_up_vertically(C1, C2)
  return C
```
