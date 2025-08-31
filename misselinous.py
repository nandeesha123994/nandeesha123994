
#swaping and fibonnaci

# #swappimg of two numbers
#
# a=10
# b=20
#
# temp=a
# a=b
# b=temp
#
# print(a,b)

#swappimg of two numbers without using the temp variable using the counter back conncept

# a=10
# b=20
#
# a=a+b #a=30
# b=a-b #b=10
# a=a-b #a=20
#
# print(a,b)

#fibonaci seires
a=0
b=1
n=int(input("enter the value of n"))
for i in range(1,n+1,1):
    print(a)  #printing the vlaue 0 first term
    c=a+b
    a=b
    b=c