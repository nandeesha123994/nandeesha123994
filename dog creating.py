# n=3
# for i in range(1,3+1,1):    #creation of tringles
#     for j in range(1,i+1,1):
#         print('*',end=' ')
#     for j in range(1,n-i+1,1):
#         print(' ',end=' ')
#     for j in range(1,n-i+1,1):
#         print(' ',end=' ')
#     for j in range(1,i+1,1):
#         print('*',end=' ')
#     print()
# n=4
# for i in range(1,4+1,1):     #creation of head
#     for j in range(1,n+1,1):
#         if i==1 or j==1 or i==4:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     for j in range(1,n-1-1+1,1):    #doubt
#         if i==4 or i==1 or j==2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
n=6
for i in range(1,6+1,1):    #creation of body
    for j in range(1,n+1,1):
        if i==1 or j==1 or i==6:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1,1):
        if i==1 or j==5 or i==6:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    # for j in range(1,n+1,1):  #creation of tale
    #     if i==5 or i==6:
    #         print('*',end=' ')
    #     else:
    #         print(' ',end=' ')
    print()
# n=3
# for i in range(1,3+1,1):   #creation of legs
#     for j in range(1,n-1+1,1):
#         print('*',end=' ')
#     for j in range(1,n-1+1,1):
#         print(' ',end=' ')
#     for j in range(1,n-1+1,1):
#         print('*',end=' ')
#     for j in range(1,n-1+1,1):
#         print(' ',end=' ')
#     for j in range(1,n-1+1,1):
#         print('*',end=' ')
#     print()