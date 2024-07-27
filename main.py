# defining function to accept users deposit.

def deposit():
    while True:

        amount = input("What amount do you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number.")
    return amount

deposit()
    

  