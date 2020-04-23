import time


def insertion_sort(A):
    """The main function for insertion sort."""
    for j in range(1, len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key
        print("Current list:\t", A)
    return A


if __name__=='__main__':
    import random
    A_in = [random.randint(10, 99) for i in range(10)]
    print("Input Array:\t", A_in, "\n")
    insertion_sort(A_in)
    print("\nAfter Sorting:\t", A_in)
