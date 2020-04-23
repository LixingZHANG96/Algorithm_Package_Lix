import time


def insertion_sort(A):
    "The main function for insertion sort."
    for j in range(len(A)):
        key=A[j]
        i=j-1
        while i>0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key
    return A


if __name__=='__main__':
    print("Input Array:", "(114, 514, 1919, 810)")
    A_in = [114,514,1919,810]
    insertion_sort(A_in)
    print("After Sorting:",A_in)
