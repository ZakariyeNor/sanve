#Building  the text based slot machine

import random

MAX_LINES = 3
MAX_BET = 120
MIN_BET = 10

#rows and columns we gonna have in our slot mechiane
ROWS = 3
COLS = 3 

#We need to specify how many symbols(characters) are in each our reels or columns
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(columns, bet_lines, bet_limit, values):
    winnings = 0
    win_line = []
    for line in range(bet_lines):
        symbol = columns[0][line] 
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet_limit
            win_line.append(lines + 1)
    return winnings, win_line
                


def get_slot_machine_spin(rows, cols, symbols):
    """
    function giving us or generating what the out come of the slot machine was using these values
    """

    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)



    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    """
    make the columns on a horizental line
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], "|", end=" ")
            else:
                print(column[row])

def deposit():
    """
    Ask the user to enter the amount of money he/she want to deposit. 
    make sure it is a number and give ValueError if it'snt. 
    Make the function generatte and run till the user inputs the right input
    """

    while True:
        amount = input("What amount of money do you want to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater then 0.")
        else:
            print("Please enter a number\n")
    return amount

def get_number_of_lines():
    """
    Collect bet lines from the user and limit the lines up to three
    """

    while True:
        lines = input("Enter the number of lines to bet on (1- " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please choose the lines you want bet")
        else:
            print((1-3))
    return lines           


def bet_limit():
    """
    Function for the requirement limit to bet on for each line
    """

    while True:
        limit = input("Choose what you would like to bet on each line: $ ")
        if limit.isdigit():
            limit = int(limit)
            if MIN_BET <= limit <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MAX_BET} - {MAX_BET} .")
        else: 
            print("Please enter a number")

    return limit


def spin(balance):

    bet_lines = get_number_of_lines()
    while True:
        bet = bet_limit()
        total_bet = bet * bet_lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on ${bet_lines} lines. Total bet is equal to: ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, win_line = check_winnings(slots, bet_lines, bet_limit, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *win_line)     
    return winnings - total_bet    

def main():
    """
    Function to call all the program
    """
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play. (q to quit)")
        if answer == 'q':
            break 
        else:
            balance += spin(balance)
    print(f"You left with ${balance}")


print("Welcome to Text Slot Mechine\n")
main()

