system_pass = 2024
account_balance = 0
user_pass = int(input("Enter the password to access your account:"))
while user_pass != system_pass:
    print("wrong password. Try again!")

    user_pass = int(input("Enter the password to access your account:"))

if user_pass == system_pass:
    while True:
        print("<<<<<<<<<<<<<<<<<Welcome to my bank management system>>>>>>>>>>>>>>>>")
        print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<>>>>>>>")
        print("choose an option to continue")
        option = int(input("1. check your account balance \n"
                           "2. withdraw\n"
                           "3. make a deposit\n"
                           "4. exit\n"
                           "0. back\n"))
        if option == 1:
            print(f"Your account balance is: GHS{account_balance}")
            add = int(input("Add an amount to activate your account"))
            account_balance = account_balance + add
            print(f"Your account is now active with a balance of: GHS{account_balance}")
            option = int(input("Enter 4 to exit or 0  to go back"))
            if option == 4:
                exit()
            elif option == 0:
                continue
        elif option == 2:
            withdraw = int(input("Enter the amount you want to withdraw"))
            account_balance = account_balance - withdraw
            print(f"Your account balance is now:GHS{account_balance}.")
            option = int(input("Enter 4 to exit or 0  to go back"))
            if option == 4:
                exit()
            elif option == 0:
                continue
        elif option == 3:
            deposit = int(input("Please Enter the amount you want to deposit"))
            account_balance += deposit
            print(f"Your account balance is now:GHS{account_balance}")
            option = int(input("Enter 4 to exit or 0  to go back"))
            if option == 4:
                exit()
            elif option == 0:
                continue
        elif option == 4:
            break
        else:
            continue








