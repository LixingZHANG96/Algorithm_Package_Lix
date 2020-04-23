## Insertrion Sort
### 1. Problem Set-up

-Input: A sequence of n numbers (a1,a2,...,an)
![Polynomial](./polynomial_expression.jpg)
-Output: A permutation (reordering) of the input sequence such
that a1<a2<...<an

-Basic idea: During every iteration, filter the smallest value in the remaining sequence and sort it to the right place.
### 2. Pseudocode
```
*BUBBLE-SORT(A)*
for i=1 to A.length-1
  for j = A.length downto i+1
    if A[j]<A[j-1] then
      exchange A[j] with A[j-1]
```
### 3. Algorithm Analysis
