import time


def horners_rule(x, A):
    """The main function for Horner's rule."""
    y = 0
    for ai in A[::-1]:
        print(ai)
        y = ai + x * y
    return y


if __name__=='__main__':
    import random
    A_in = [random.randint(10, 99) for i in range(5)]
    x = 2
    print("Input Parameters:\t", A_in)
    print("x = 2")
    y = horners_rule(x, A_in)
    print("Calculation Result:\t", y)
