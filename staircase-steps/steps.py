"""How many different ways can you climb a staircase of `n` steps?

You can climb 1, 2, or 3 steps at a time.

For one step, we could do this one way: 1

    >>> steps(1)
    1

For two: 11 2

    >>> steps(2)
    2

For three: 111 12 21 3

    >>> steps(3)
    4

For four: 1111 121 211 112 22 13 31

    >>> steps(4)
    7

For five: 11111 2111 1211 1121 1112 122 212 221 113 131 311 23 32

    >>> steps(5)
    13

For six steps: 111111 21111 12111 11211 11121 11112 2211 2121 2112
    1212 1122 1221 3111 1311 1131 1113 321 312 213 231 132 123 222 33

    >>> steps(6)
    24
"""

from math import factorial


def product(l):
    """Definition of product. 

    Like sum, except for multiplication.
    """

    product = 1
    for i in l:
        product *= i
    return product


def steps(n):
    """How many different ways can you climb a staircase of `n` steps?

    You can climb 1, 2, or 3 steps at a time.
    """

    init3s = n // 3
    init2s = (n % 3) // 2
    init1s = (n % 3) % 2

    # Construct an array of the values of the variables in 3*a + 2*b + c = n
    array = [init3s, init2s, init1s]
    possibilities = 0

    while True:
        # This is a combinatorics problem, allowing us to solve this with a
        # high degree of efficiency in both space and time.
        #
        # To explain this, let's look at the example 32211 to climb 9 stairs.
        #
        # That is (1 step) * 3 + (2 steps) * 2 + (2 steps) * 1
        # => 5 steps => 5 digits
        #
        # The number of possible `permutations` of 5 unique things is 5! = 120
        # However, we should eliminate possibilities because we have repeated
        # the digits 2 and 1 twice each in this example.
        #
        # To eliminate repeated digits, we want to remove 2! permutations of 2
        # digits per permutation, for the digits in [1, 2]
        #
        # This results in the expression:
        #
        #             (number_digits)!
        #   ---------------------------------
        #   (num_1s)! * (num_2s)! * (num_3s)!
        #
        # For each set of digits.
        #
        # We count down from the maximum number of 3's to the case of all 1's
        # to get each set of digits, adding to the accumulator `possibilities`.

        num = factorial(sum(array))
        den = product([factorial(count) for count in array])
        possibilities += num // den
        if array[1] > 0:
            array[1] -= 1
            array[2] += 2
        elif array[0] > 0:
            array[0] -= 1
            array[1] = (n - (3 * array[0])) // 2
            array[2] = (n - (3 * array[0])) % 2
        else:
            return possibilities


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED! YOU'RE A STAIRMASTER!\n")
