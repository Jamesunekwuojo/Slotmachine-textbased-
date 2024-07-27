# CONSTANTS DEFINITION using capital  letters for my variable which is a conventional way for declaring python constants
MAX_LINES =3 

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

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on(1 -"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0:
                break
            else: 
                print("Amount must be greater than zero")
        else:
            print("Please enter a number.")
    return amount


def main():

    balance = deposit()

    main()
    

  