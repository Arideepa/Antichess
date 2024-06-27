# Antichess

Antichess is a variation of chess where the goal is to sacrifice all your pieces before your opponent.

## Rules of Antichess

- The board and piece movements are identical to traditional chess.
- The objective is to deliberately lose all your pieces before your opponent.
- If a player can capture a piece, they must do so; if multiple captures are possible, they choose which piece to take.

# Backend Chess Game

This project implements a backend chess game system with RESTful API endpoints for game management and state tracking.

## API Endpoints

- **Start a New Game**: `POST /api/game/start`
  - Initializes a new chess game and returns the initial board state.

- **Make a Move**: `POST /api/game/move`
  - Sends a move request to update the game state based on player input.

- **Undo Move**: `POST /api/game/undo`
  - Reverts the last move made in the game.

- **Get Board State**: `GET /api/game/board`
  - Retrieves the current board state to render in the frontend.

- **Check Game Status**: `GET /api/game/status`
  - Checks the game's current status (e.g., ongoing, checkmate).



## Getting Started

### Running the Program

1. **Clone the Repository:**

   git clone https://github.com/your-username/Antichess.git
   cd Antichess
   
3. **Install Python:**
   
   Make sure Python 3.x is installed on your system. You can download Python from python.org.

5. **Run the Program:**
   
   python chess_game.py
   Interacting with the Program:

   Input moves in the format "e2 e4" to make a move.
   Type display to show the current board state.
   Type undo to reverse the last move.
   Type quit to exit the game.
   Contributing
   Contributions, bug reports, and feature requests are welcome! Please follow these steps:

Additional Instructions
Dependencies: This project does not require any external dependencies beyond Python itself.
Troubleshooting: If you encounter issues, check that Python is installed correctly and that you're running the program in a compatible environment.
