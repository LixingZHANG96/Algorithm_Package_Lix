## Merge Sort
### 1. Problem Set-up

-Input: A sequence of n numbers (a1,a2,...,an)

-Output: A permutation (reordering) of the input sequence such
that a1<a2<...<an
### 2. Pseudocode
```
*MERGE-SORT(List,start,end)*
if start<end
  middle=floor((start+end)/2)
  MERGE-SORT(List,start,middle)
  MERGE-SORT(List,middle+1,end)
  MERGE(List,start,middle,end)
```
```
*MERGE(List,start,middle,end)*
  length_left=middle-start+1
  length_right=end-middle
  let L be an array of length length_left+1
  let R be an array of length length_right+1
  for i=1 to length_left
    L[i]=A[start+i-1]
  for i=1 to length_right
    R[i]=A[middle+i]
  L[length_left+1]=+Inf
  R[length_right+1]=+Inf
  i=1
  j=1
  for k=start to end
    if L[i]≤R[j] then
      List[k]=L[i]
      i=i+1
    else
      List[k]=R[j]
      j=j+1
```
### 3. Algorithm Analysis
