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
        print("After Merge:\t",A)


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


if __name__=='__main__':
    import random
    A_in = [random.randint(10, 99) for i in range(10)]
    print("Input Array:\t", A_in,'\n')
    Merge_Sort(A_in)
    print("\nAfter Sorting:\t", A_in)
