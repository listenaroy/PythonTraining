#Python至此不支援switch
if True:
    print("True")

if False:
    print("True")

if True:
    print("True")
else:
    print("False")

if False:
    print("True")
else:
    print("False")

#判斷式
x=input("Please in put a number: ")
x=int(x)
if x>200:
    print(">200")
elif x>100:
    print("100<x<200")
else:
    print("<100")

#Example 2 
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
op=input("Enter +,-,*,/")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)    
elif op=="/":
    print(n1/n2)    
else:
    print("No support!") 

    