str1=input("enter the string 1")
str2=input("enter the string 2")
mark=0



if (len(str1)!=len(str2)):
    mark=1

else:
    n=len(str1)
    for i in range(0,n-1+1,1):
        if str1[i]!=str2[i]:
            mark = 1
            break
if mark==0:
    print("it is equal")
else:
    print("not equal")


