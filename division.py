
a=100
print(f"Initial value of a = {a}")
b = a/10
print(f"after divsion valye of b = {b}")
qw=256
print(f"Initial value of qw ={qw}")
hj =qw/16
print(f"initial value of hj ={hj}")

i = 20333
iold = i
j=1
with open("multiplication.txt","w+") as f:
    while(i<22444444):
        #f.write(f"{iold}*{j}={i}\n")
        print(f"iold = {iold}, a = {a},i = {i}, hj= {hj}, j = {j}")
        hj = iold+ 10
        hj=a+b*hj
        if (i > 40666):
            break

        j=45*i/j
        i=i+iold
f.close()