# Flask Slot Machine

This project is a web-based slot machine game built using Flask. It provides a user-friendly interface for players to interact with the slot machine in real-time.

## Project Structure

```
flask-slot-machine
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── main.py              # Contains the main logic for the slot machine
│   ├── static
│   │   ├── css
│   │   │   └── styles.css   # CSS styles for the web interface
│   │   └── js
│   │       └── scripts.js    # JavaScript for handling user interactions
│   └── templates
│       └── index.html       # Main HTML template for the web interface
├── requirements.txt          # Lists project dependencies
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-slot-machine
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python -m app
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to access the slot machine game.

## Usage Guidelines

- Place your bets using the interface.
- Click the "Spin" button to play the game.
- The results will be displayed in real-time, showing your winnings and the outcome of each spin.

Enjoy your game!