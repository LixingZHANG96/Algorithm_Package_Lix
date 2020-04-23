import time
import math


def Merge_Sort(A, start=1, end=-1):
    """Main function for merge sort."""
    if end == -1:
        end = len(A)
    if start < end:
        middle = math.floor((start+end)/2)
        Merge_Sort(A, start, middle)
        Merge_Sort(A, middle+1, end)
        Merge(A, start, middle, end)


def Merge(A, start, middle, end):
    """Merge 2 sorted arrays into one sorted array."""
    Inf_local = max(A)+1
    L = A[start-1:middle]
    L.append(Inf_local)
    R = A[middle:end]
    R.append(Inf_local)
    i = 0
    j = 0
    for k in range(start-1, end):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    print(A)


if __name__=='__main__':
    print("Input Array:", "(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)")
    A_in = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    Merge_Sort(A_in)
    print("After Sorting:", A_in)
