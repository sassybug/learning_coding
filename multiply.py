def multiply(a,b) :
    return a*b

a=float(input("user enter any int or float"))
b=float(input("user enter second int or float"))
c=int(input("user press 1 and I will multiply"))
result=5
if c==1 :
   result=multiply(a,b)

   print(f"Solution to your qestion={result}")