#palindrome number
n=int(input(""))
save=n  #saving the original nuber fro comparing left to right
rev=0  #storing the number from right to legt
#(save==rev is palindrome)
while(n!=0):
    r=n%10
    n=n//10
    rev=rev*10+r
if save==rev:
    print("palindrome")
else:
    print("not a palindrome")

#why not n is because n become a 0 when we destruction