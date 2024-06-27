# Antichess
Anti-chess, a variation of chess, uses the same board and piece movements as traditional chess. The objective is to deliberately lose all your pieces before your opponent. If a player can capture a piece, they must do so; if multiple captures are possible, the player chooses which piece to take.

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
  - Checks the current status of the game (e.g., ongoing, checkmate).

