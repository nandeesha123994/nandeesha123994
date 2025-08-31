n=int(input("enter the size of list"))
l=[]
i=0
while i<n:
    num=int(input("enter a number"))
    l.insert(i,num)
    i=i+1
print(l)

def even(num):
    if num%2==0:
        return True
    else:
        return  False


# i=0
# while(i<=4):
#     data=l[i]
#     choice=even(data)
#
#     if choice==True:
#         print("even numbers are",l[i])
#
#     i=i+1


res=list(filter(even,l))
print(res)