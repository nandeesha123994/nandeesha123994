ptr=open("car.jpeg","rb")
data=ptr.read(33789)
print(data)
ptr.close()

ptr1=open("newcar.jpeg","wb")
ptr1.write(data)
# print(ptr1)
ptr1.close()