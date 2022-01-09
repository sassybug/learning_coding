


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def exponent(a,b):
    return a**b

a = float(input("enter any nnumber "))
b = float(input("enter second number "))
c = int(input ("Press 1 for add, 2 for subtract, 3 for multiply, 4 for divide, 5 for exponent "))

result = -1

if c == 1:
    result = add(a,b)
if c == 2:
    result = subtract(a,b)
if c==3 :
   result = multiply(a,b)
if c==4 :
   result = divide(a,b)

if c==5 :
   result = exponent(a,b)
print(f"Solution to your question is {result}")