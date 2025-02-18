from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    columns = [random.sample(all_symbols, rows) for _ in range(cols)]
    return columns

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        if all(column[line] == columns[0][line] for column in columns):
            winnings += values[columns[0][line]] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

@app.route('/', methods=['GET', 'POST'])
def index():
    balance = 100
    winnings = 0
    winning_lines = []
    slots = []

    if request.method == 'POST':
        lines = int(request.form['lines'])
        bet = int(request.form['bet'])
        total_bet = bet * lines

        if total_bet <= balance:
            slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
            winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
            balance += winnings - total_bet

    return render_template('index.html', balance=balance, winnings=winnings,
                           winning_lines=winning_lines, slots=slots)

if __name__ == '__main__':
    app.run(debug=True)


# sokoro@aul.edu.ng