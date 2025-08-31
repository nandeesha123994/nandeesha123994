#finding the length of a number
len=0
n=int(input("enter the vlaue of n"))
save=n

while(n!=0):
    r=n%10
    n=n//10
    len=len+1
n=save

sum=0
while(n!=0):
    r = n % 10
    n = n // 10
    sum=sum+(r**len)  #sucssesive calcualtion
print(sum)

if sum==save:   #comparision
    print("palindrome")
else:
    print("not a palindrome")

