
import random
num=random.random()                                   # generatint 0 to 1#
print(num)

num=random.uniform(1,1000)                       #floating value
print(num)

num=random.randint(1,100)                       #int value
print(num)

num=random.randrange(2,100,2)           #give even or odd val
print(num)

num=random.randrange(1,100,2)
print(num)

num=random.sample(range(1,100),5)                     #sequence val
print(num)