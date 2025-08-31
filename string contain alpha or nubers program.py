str=input("enter the string")

print(str)

if str.isalpha():
    print("string contains alphabets only")
elif str.isdigit():
    print("string contains only digits")
elif str.isalnum():
    print("string contaims both")
else:
    print("string contains other characters also")