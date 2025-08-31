#reversing the string using

# str=input("enter  a string")
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)
#

#another method to reversong the string

# str=input("enter the string")
# rev=str[ : :-1]
# print(rev)

text = input("enter a string")
words = text.split()          # Split into list of words
rev = " ".join(words[::-1])   # Reverse the list and join back
print(rev)


