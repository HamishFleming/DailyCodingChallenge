#!/usr/bin/env python3
"""
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2


"""
# Notes:
# get length of the array
# Errorhandeling for odd/one entry


__author__ = "Hamish Fleming"
__version__ = "0.0.1"
__license__ = "MIT"


tempr = [] 

# Function Funtionality: Nothing fancy, loads in the array and itterates over each value one at a time by 'feeding' it to the spicey funcitonality 
def feed(arr):
    for i in range(len(arr)):
        tempr.append(arr[i])
        middle_two(tempr)
        
# Function: Takes in An Array
def middle_two(arr):
    temp = []
    temp.extend(arr)
    temp.sort()
    #use mod to detect if the length of the list is even
    if (len(temp)%2 == 0):
        # This could probably be cleaned up
        middle = (temp[int(len(arr)/2)-1]+temp[int(len(arr)/2)])/2
    else:
        middle = temp[int(len(arr)/2)-1]
    print(middle)

def main():
    """ Main entry point of the app """
    arraylist=[2, 1, 5, 7, 2, 0, 5]
    feed(arraylist)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()


