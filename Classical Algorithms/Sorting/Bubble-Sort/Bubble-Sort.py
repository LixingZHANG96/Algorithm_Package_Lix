import time


def bubble_sort(A):
    """The main function for bubble sort."""
    for i in range(len(A)-1):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                cache = A[j]
                A[j] = A[j-1]
                A[j-1] = cache
        print("Current list:\t", A)
    return A


if __name__=='__main__':
    import random
    A_in = [random.randint(10, 99) for i in range(10)]
    print("Input Array:\t", A_in)
    bubble_sort(A_in)
    print("After Sorting:\t", A_in)
