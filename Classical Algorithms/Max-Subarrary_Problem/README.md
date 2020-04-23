## The Max-subarray Problem
### 1. Problem Set-up

- Description: Given an array of different values of increment/decrement, find out the sequence in which the total increment is the largest.

- Idea: For any sequence **S**, divide it into 2 halves **L** and **R**. The max-subarray of **S** would be possibly,
 1. A sequence crossing the middle point of **S**.
 2. A sub-sequence of sequence **L**.
 3. A sub-sequence of sequence **R**.

  for case 2 and 3, recursively find the max-subarray of their subarray, and return the largest to the parent level.

- Input: The value for **x** and all its efficients.

- Output: Calculate the polynomial expression:

### 2. Pseudocode
```
*FIND-MAX-SUBARRAY(S, start, end)*
  if high = low then
    return(start, end, S[start])
  else
    middle = floor((start + end) / 2)
    (left_start, left_end, left_sum) = FIND-MAX-SUBARRAY(S, start, middle)
    (right_start, right_end, right_sum) = FIND-MAX-SUBARRAY(S, middle+1, end)
    (cross_start, cross_end, cross_sum) = FIND-MAX-CROSSING-SUBARRAY(S, start, middle, end)
    max_sum = max(left_sum, right_sum, cross_sum)
    return (max_start, max_end, max_sum)
```
```

*FIND-MAX-CROSSING-SUBARRAY(S, start, middle, end)*
  left_sum = -∞
  sum = 0
  for i = middle downto start
    sum = sum + S[i]
    if sum > left_sum then
      left_sum = sum
      max_left = i
  right_sum = -∞
  sum = 0
  for i = middle to end
    sum = sum + S[i]
    if sum > right_sum then
      right_sum = sum
      max_right = i
  return (max_left, max_right, left_sum+right_sum)
```
### 3. Algorithm Analysis
