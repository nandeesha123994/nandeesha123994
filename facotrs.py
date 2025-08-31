#factors
# n=int(input("enter the value of n"))
# for i in range(1,n+1,1):
#     if n%i==0:
#         print(i,end=" ")

# counting the 10th factors
# n=int(input("enter he value of n"))
# count=0
# for i in range(1,n+1,1):
#     if n%i==0:
#         count=count+1
# print(count)

#common factors finding

# a=int(input("enter a vlaue of a"))
# b=int(input("enter the vlaue of b"))
#
# for i in range(1,a+1,1): #u can take a and b also both common factors are same
#     if a%i==0 and b%i==0:
#         print(i)

#printing the huf value
# a=int(input("enter a vlaue of a"))
# b=int(input("enter the vlaue of b"))
# hcf=0
# for i in range(1,a+1,1): #u can take a and b also both common factors are same
#     if a%i==0 and b%i==0:
#         hcf=i          #hcf will store 1,5 and  it will print last number as hcf
# print("hcf=",hcf)



a=int(input("enter a vlaue of a"))
b=int(input("enter the vlaue of b"))
hcf=0
for i in range(1,a+1,1): #u can take a and b also both common factors are same
    if a%i==0 and b%i==0:
        hcf=i          #hcf will store 1,5 and  it will print last number as hcf
print("hcf=",hcf)
lcm=a*b//hcf
print("lcm=",lcm)















