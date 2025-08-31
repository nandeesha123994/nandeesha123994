'''
# empty squre pattern

for i in range(1,5+1,1):
    for j in range(1,5+1,1):
        if i==1 or i==5 or j==1 or j==5:
            print("* ",end="")
        else:
            print("  ",end="")
    print("")

'''
'''
#regular diagonal i===j

 for i in range(1,5+1,1):
     for j in range(1,5+1,1):
         if i==j:
             print("* ",end="")
         else:
             print("  ",end="")
    print("")
    
'''
'''
#cross diagonal
n=5
for i in range(1, 5 + 1, 1):
    for j in range(1, 5 + 1, 1):
        if i+j == n+1:
            print("*", end="")
        else:
            print("  ", end="")
    print("")
'''
'''
#halo triangle
n=5
for i in range(1, 5 + 1, 1):
    for j in range(1, 5 + 1, 1):
        if i==5 or j==5 or i+j == n+1:   #i==5 or j==5 or i+j == n+1
            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")
    '''
'''
#inverted halo triangle
n=5
for i in range(1, 5 + 1, 1):
    for j in range(1, 5 + 1, 1):
        if i==1 or j==5 or i==j:  #i==1 or j==5 or i==j
        
            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")
'''

'''
n = 5
for i in range(1, 5 + 1, 1):
    for j in range(1, 5 + 1, 1):
        if i == 1 or j ==1 or i==5 or j==5 or i==j or i+j==n+1:

            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")
'''


'''
n = 5
for i in range(1, 5 + 1, 1):
    for j in range(1, 5 + 1, 1):
        if i == 1 or j ==1 or i==5 or j==5 or i==j :

            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")
'''

'''
n = 5
for i in range(1, 5 + 1, 1):
    for j in range(1, 5 + 1, 1):
        if i == 1 or j ==1 or i==5 or j==5 or i+j==n+1 :

            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")
'''

'''

for i in range(1, 5 + 1, 1):
    for j in range(1, 5 + 1, 1):
        if i == 1 or j ==1 or i==5 or j==5 or j==3  :

            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")

'''

'''
for i in range(1, 5 + 1, 1):
    for j in range(1, 5 + 1, 1):
        if i == 1 or j ==1 or i==5 or j==5 or i==3  :

            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")
'''
'''

n=11
for i in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):
        if i==1 or i==11 or j==1 or j==11 or i+j==n+1 or i==j or i==6 or j==6:
            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")
    
    '''
'''
n=11
for i in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):
        if  i+j==n+1 or i==j or i==6 or j==6:
            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")
    
'''
'''
n = 5
for i in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):
        if i + j == n + 1 or i == j :
            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")
'''
'''
n=11
for i in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):
        if   i==6 or j==6:
            print("* ", end="")
        else:
            print("  ", end="")
    print(" ")
    '''







