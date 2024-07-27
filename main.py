# CONSTANTS DEFINITION using capital  letters for my variable which is a conventional way for declaring python constants
MAX_LINES =3 
MAX_BET = 100
MIN_BET =1

# defining function to accept players deposit.
def deposit():

    while True:
        amount = input("What amount do you like deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f"Amount must be between greeter than zero")
        else:
            print("Please enter a number.")
    return amount



def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on(1 -"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines <= MAX_LINES:
                break
            else: 
                print("Enter valid number of lines")
        else:
            print("Please enter a number.")
    return lines




def get_bet():

    while True:
        amount = input("What amount do you like to bet on each line ? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<=amount<=MAX_BET :
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")
    return amount

def main():

    balance = deposit()

    lines = get_number_of_lines()

    bet = get_bet()

    total_bet = bet * lines

    while True:
        if total_bet < balance:
            break
        else:
            print(f"You don't have sufficient balance to bet on that amount, your total balance is ${balance}.")

    

    print(f"You are betting ${bet} on ${lines} lines, total bet is equal to ${total_bet} ")
    

  

   

main()
    

  