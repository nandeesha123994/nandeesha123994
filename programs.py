#wpp to check the buzz number

# n=int(input("enter the vlaue of n"))
#
# if n%7==0 or n%10==7:
#   print(n,"is buzz number")
# else:
#   print(n,"is not a buzz number")


#wpp to check where the number is spy number or not

# n=int(input("enter the vlaue of n"))
# sum=0
# pro=1
#
# while(n>0):
#     r=n%10
#     sum=sum+r
#     pro=pro*r
#     n=n//10
#
# print(sum)
# print(pro)
#
# if sum==pro:
#     print("is a spy number")
# else:
#     print("is not spy number")
#


#wpp to chech the arshad number(naiven number)
#a number is divisible by sum od its digits

# n=int(input("enter a number"))
# temp=n                                                                 #why we need to store the original value into a temp beacuse n become zero
# sum=0
#
# while n>0:
#     r=n%10
#     sum=sum+r
#     n=n//10                                                            #n becomes zero
# print(sum)
# print(n)
# print(temp)
# if temp%sum==0:
#     print("number is arsahd number ")
# else:
#     print("number is not a arshad number")
#


#wpp to add sum of even digits and odd digits

# n=int(input("enter the value of n"))
# sumeven=0
# sumodd=0
#
# while(n>0):
#     r=n%10
#     if r%2==0:
#         sumeven=sumeven+r
#     else:
#         sumodd=sumodd+r
#     n=n//10
#
# print(sumeven)
# print(sumodd)


#wpp to add even pos and oddpos vaalues

# n=(input("enter a vlaue"))
# evenpos=0
# oddpos=0
# pos=len(n)
# num=int(n)
#
# while num>0:
#     r=num%10
#     if pos%2==0:
#         evenpos=evenpos+r
#     else:
#         oddpos=oddpos+r
#     num=num//10
#     pos=pos-1
#
# print(evenpos)
# print(oddpos)