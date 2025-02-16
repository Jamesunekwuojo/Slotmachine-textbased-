from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

ROWS = 3
COLS = 3
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
}
symbol_value = {
    "A": 5,
    "B": 3,
    "C": 1,
}

def get_slot_machine_spin(rows, cols, symbol_count):
    symbols = []
    for symbol, count in symbol_count.items():
        symbols.extend([symbol] * count)
    return [[random.choice(symbols) for _ in range(cols)] for _ in range(rows)]

def check_winnings(slots, lines, bet, symbol_value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        if all(slot == slots[0][0] for slot in [slots[line][col] for col in range(len(slots[line]))]):
            winnings += symbol_value[slots[line][0]] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin', methods=['POST'])
def spin():
    lines = int(request.form.get('lines'))
    bet = int(request.form.get('bet'))
    total_bet = lines * bet
    balance = 100  # Example balance, replace with actual user balance logic

    if total_bet > balance:
        return jsonify({'error': "Insufficient balance."})

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    return jsonify({
        'slots': slots,
        'winnings': winnings,
        'winning_lines': winning_lines,
        'balance': balance - total_bet + winnings
    })

if __name__ == '__main__':
    app.run(debug=True)