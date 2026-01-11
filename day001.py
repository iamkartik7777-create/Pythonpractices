pin = int(input("Enter your password: "))
balance = 10000
if pin == 12345:
    print("Enter ATM")
    atm = int(input("Enter 1 for Withdrawal, 2 for Deposit, 3 for Balance Check: "))

    if atm == 1:
        amount = int(input("Enter Amount: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance:", balance)
        else:
            print("Invalid amount")

    elif atm == 2:
        amount = int(input("Deposit amount: "))
        if amount > 0:
            balance = balance + amount
            print("Deposit Successful")
            print("Updated Balance:", balance)
        else:
            print("Invalid deposit amount")

    elif atm == 3:
        print("Your Balance:", balance)

    else:
        print("Invalid choice")

else:
    print("Incorrect password")

    
