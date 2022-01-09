a_inches:float=float(input("Enter the input"))
if type (a_inches) is not float:
   print("Hey user this is mathemitcal inches not string.Please dont  enter any names")
a_feet =round(a_inches/12,6)
print (f"out put in feet={a_feet}")