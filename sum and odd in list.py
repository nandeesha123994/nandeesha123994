a=[]
evensum=0
oddsum=0
n=int(input("enter the size os a string"))

for i in range(0,n-1+1,1):
    x=int(input("enter teh numbers"))
    a.append(x)

for i in a:
    if i%2==0:
        oddsum=oddsum+i
        print(sum)
    else:
        evensum=evensum+i
        print(evensum)


