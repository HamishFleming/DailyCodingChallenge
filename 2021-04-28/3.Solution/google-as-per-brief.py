#!/usr/bin/env python3
"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

__author__ = "Hamish Fleming"
__version__ = "0.0.1"
__license__ = "MIT"


def lefunc(array, k):
    for i in range(len(array)):
        target = k - array[i]
        for j in array:
            if array[j-1] == target:
                print("found one match: " + str(array[i]) + " And: " +  str(array[j-1]) + " = " + str(k))
                # Break on first instance of two elements equaling k,and return true as per the brief
                return True




def main():
    """ Main entry point of the app """
    k = input("Please enter 'k': ")
    print("\n")
    # Read in range of values
    input_string = input("Enter elements  with spaces")
    print("\n")
    user_list = input_string.split()
    print("List: ", user_list)
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
    lefunc(user_list, int(k))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()