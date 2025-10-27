# n=int(input("enteer the number do want to check"))
# count=0
#
# for i in range(1,n+1,1):
#     if n%i==0:
#         count+=1
#
# if count==2:
#     print("prime number")
# else:
#     print("not a prime number")


#prime numbers from 1 to 100
n=101

for i in range(1,n+1,1):
    count = 0
    for j in range(1,n+1,1):
        if i%j==0:
            count+=1

    if count==2:
        print(i,end=" ")
