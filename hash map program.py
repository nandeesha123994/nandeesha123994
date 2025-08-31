pos=[0 for i in range(10)]
neg=[0 for i in range(10)]


n=int(input("enter the size:"))
for i in range(0,n-1+1,1):
    x=int(input("enter the numbers"))
    if x>=0:
        pos[x]=pos[x]+1
    else:
        x=x*-1             #here converting negative input value into positive value because negative index nubers are not there
        neg[x]=neg[x]+1

print(pos)
print(neg)


x=int(input("enter the nuber to be search"))
if x>=0:
    print(pos[x])
else:
    x=x*-1
    print(neg[x])

print("number -   count")

# for i in pos:        #countitng the number of times a each number occur in  positive list(here only counted which number is repeated)
#     if(pos[i]!=0):
#         print(i," ",pos[i])
# for i in neg:        #countitng the number of times a each number occur in  negative  list(here only counted which number is repeated)
#     if(neg[i]!=0):
#         print(i*-1," ",neg[i])







