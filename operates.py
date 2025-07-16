select=input("enter the opertations:-(add,sub,mul) ")
num1=int(input("enter the vlaue of num1"))
num2=int(input("enter the vlaue of num1"))
if select=="add":
    print("addition of two numbers is " ,num1+num2)
elif select=="sub":
    print("subtraction of two numbers ",num1-num2)
elif select=="mul":
    print("multiplication of two numbers ",num1*num2)
else:
    print("enter the valid operations")