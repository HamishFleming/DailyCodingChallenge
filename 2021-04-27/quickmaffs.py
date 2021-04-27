#!/usr/bin/env python3
"""
Amazon Hiring Question, sample problem

There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X. 
"""

__author__ = "Hamish Fleming"
__version__ = "0.0.1"
__license__ = "MIT"

# Fibonacii but _fast_
def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]


def main():
    """ Main entry point of the app """
    steps = int(input("steps: "))
    input_string = input('Enter elements of X separated by space ')
    print("\n")
    user_list = input_string.split()
    # print list
    print('X: ', user_list)
    # convert each item to int type
    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = int(user_list[i])
    print(staircase(steps,(user_list)))



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()