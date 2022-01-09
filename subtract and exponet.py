def exponet(a,b) :
    return a**b

def subtract(a,b) :
     return a-b

a=float(input("user enter any number" ))
b=float(input("user enter any number"))
c=int(input("user press 1 to exponet,press 2 to subtract"))
result=-9
if c==1:
   result= exponet(a,b)
if c==2 :
     result=subtract(a,b)

print(f"Solution to your qwestion={result}")


