#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Hamish Fleming"
__version__ = "0.0.1"
__license__ = "MIT"





def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(fun):
    return fun.__closure__[0].cell_contents
def cdr(fun):
    return fun.__closure__[1].cell_contents


def main():
    """ Main entry point of the app """
    var = cons(5,7)
    # As per brief: car(cons(3,4))
    print(car(cons(3,4)))
#   print(var.__closure__[0].cell_contents)
    print('Last Value: ' + str(cdr(var)) + '\nFirst Value: '+ str(car(var)))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()



