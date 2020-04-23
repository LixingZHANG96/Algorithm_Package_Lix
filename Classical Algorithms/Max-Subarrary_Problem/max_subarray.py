import time
import math


def max_subarray(S, start=0, end=-1):
    """The main function for the max-subarray problem."""
    if end<0:
        end = len(S)-1
    if end == start:
        return (start, end, S[start])
    else:
        middle = math.floor((start+end)/2)
        (left_start, left_end, left_sum) = max_subarray(S, start, middle)
        (right_start, right_end, right_sum) = max_subarray(S, middle+1, end)
        (cross_start, cross_end, cross_sum) = max_crossing_subarray(S, start, middle, end)
        if left_sum > cross_sum or right_sum > cross_sum:
            if left_sum > right_sum:
                return (left_start, left_end, left_sum)
            else:
                return (right_start, right_end, right_sum)
        return (cross_start, cross_end, cross_sum)


def max_crossing_subarray(S, start, middle, end):
    left_sum = S[middle]
    max_left = middle
    right_sum = S[middle + 1]
    max_right = middle + 1
    sum = left_sum
    for i in range(middle-1, start-1, -1):
        sum += S[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    sum = right_sum
    for i in range(middle+2, end+1):
        sum += S[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    print("The max cross subarray for sequence:\t", S[start:middle], S[middle:middle+2], S[middle+2:end+1])
    print("is:\t\t\t\t\t", S[max_left:max_right+1])
    return (max_left, max_right, left_sum+right_sum)


if __name__=='__main__':
    import random
    A_in = [random.randint(-20, 20) for i in range(20)]
    print("Input Parameters:\t", A_in)
    (max_start, max_end, max_sum) = max_subarray(A_in)
    print("The final max subarry:", A_in[max_start:max_end+1])
    print("with a summation of:", max_sum)
