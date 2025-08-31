username='nandi'
password=123
balance=10

while True:

    user=input("Enter the user name")
    passs=int(input("Entert he password"))

    if user==username and passs==password:
        while True:
            print("your login is succesfull")
            print('''
            1.Deposit
            2.withdrawal
            3.blance
            4.exit''')
            choice = int(input("select your choice"))
            if choice==1:
                amu=int(input("enter the amount you want deposit "))
                print("your amount is deposited sussesefully",amu)
                balance=balance + amu
            elif choice==2:
                withdr=int(input("enter the amount you want withdrwal "))
                print("your amount is succesufully withdrwed",withdr)
                balance=balance-withdr
            elif choice==3:
                print("your current balnce is",balance)
            elif choice==4:
              exit()

            else:
               print("enter the correct credential")