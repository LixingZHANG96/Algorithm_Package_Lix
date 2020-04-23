## Insertrion Sort
### 1. Problem Set-up

-Input: A sequence of n numbers (a1,a2,...,an)

-Output: A permutation (reordering) of the input sequence such
that a1<a2<...<an
### 2. Pseudocode
```
*INSETION-SORT(A)*
for j=2 to A.length
  key=A[j]
  i=j-1
  while i>0 and A[i]>key
    A[i+1]=A[i]
    i=i-1
  A[i+1]=key
```
### 3. Algorithm Analysis
