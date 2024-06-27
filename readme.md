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

## Integration Steps

### Step 1: Set Up Frontend Project

Clone the frontend repository and install dependencies:

```bash
git clone https://github.com/your-frontend-repo.git
cd your-frontend-repo
npm install
