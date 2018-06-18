"""

Implementations of various primality tests

"""

def fermatTest(number):
    
    if pow(2, number - 1, number) == 1:
        return str(number) + " is Probably Prime."
    if pow(2, number - 1, number) != 1:
        return str(number) + " is Certainly Composite."



