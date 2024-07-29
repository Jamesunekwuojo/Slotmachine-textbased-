import random

# CONSTANTS DEFINITION using capital  letters for my variable which is a conventional way for declaring python constants
MAX_LINES =3 
MAX_BET = 100
MIN_BET =1


# NUMBERS OF ROWS AND COLUMNS FOR SLOT MACHINE
ROWS = 3
COLS =3 #columns same as reels in slot machine

symbol_count = { #This is a dictonary in python  
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,

}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =[] #This is a lsit
    #for loop to ilterate the dictionary

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol):
            all_symbols.append(symbol) 
    
    columns = []

    for _ in range(cols):
        column = []

        current_symbols = all_symbols[:] #making a copy of all_symbols  using the slice operator in other to make it more flexible

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column) 
    
    return columns
     

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

    

  

    while True:
        bet = get_bet()

        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have sufficient balance to bet on that amount, your total balance is ${balance}.")
        else:
            break
 

    print(f"You are betting ${bet} on ${lines} lines, total bet is equal to ${total_bet} ")
    

  

   

main()
    

  