"""
Docstring for main2
Unit test = Smallest type of test and it's typically testing one very small component of code

"""

def add(a,b):
    return a + b

def divide(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a / b
