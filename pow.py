import math


def pow(x:int,y:int) -> int:
    """
    This program gives x power y
    :param x: int: One of input variable
    :param y: int: Second input variable
    :return: int: Product of two numbers
    """
    return x**y
b=1
a = 1
x=float(input("user enter any number\n"))
y=float(input("user enter number of power\n"))
print(f"Solution to ={math.pow(x, y)}")