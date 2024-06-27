class Piece:
    def __init__(self, color):
        self.color = color

    def get_moves(self, board, row, col):
        raise NotImplementedError("This method should be implemented by subclasses")

    def __str__(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def is_capturing_move(self, board, row, col, target_row, target_col):
        target_piece = board[target_row][target_col]
        return target_piece is not None and target_piece.color != self.color


class King(Piece):
    def __str__(self):
        return 'K' if self.color == 'white' else 'k'

    def get_moves(self, board, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        moves = []
        for dr, dc in directions:
            if 0 <= row + dr < 8 and 0 <= col + dc < 8:
                target_piece = board[row + dr][col + dc]
                if target_piece is None or target_piece.color != self.color:
                    moves.append((row + dr, col + dc))
        return moves


class Queen(Piece):
    def __str__(self):
        return 'Q' if self.color == 'white' else 'q'

    def get_moves(self, board, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        moves = []
        for dr, dc in directions:
            r, c = row, col
            while 0 <= r + dr < 8 and 0 <= c + dc < 8:
                r += dr
                c += dc
                target_piece = board[r][c]
                if target_piece is None:
                    moves.append((r, c))
                elif target_piece.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
        return moves


class Rook(Piece):
    def __str__(self):
        return 'R' if self.color == 'white' else 'r'

    def get_moves(self, board, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        moves = []
        for dr, dc in directions:
            r, c = row, col
            while 0 <= r + dr < 8 and 0 <= c + dc < 8:
                r += dr
                c += dc
                target_piece = board[r][c]
                if target_piece is None:
                    moves.append((r, c))
                elif target_piece.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
        return moves


class Bishop(Piece):
    def __str__(self):
        return 'B' if self.color == 'white' else 'b'

    def get_moves(self, board, row, col):
        directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        moves = []
        for dr, dc in directions:
            r, c = row, col
            while 0 <= r + dr < 8 and 0 <= c + dc < 8:
                r += dr
                c += dc
                target_piece = board[r][c]
                if target_piece is None:
                    moves.append((r, c))
                elif target_piece.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
        return moves


class Knight(Piece):
    def __str__(self):
        return 'N' if self.color == 'white' else 'n'

    def get_moves(self, board, row, col):
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        moves = []
        for dr, dc in directions:
            if 0 <= row + dr < 8 and 0 <= col + dc < 8:
                target_piece = board[row + dr][col + dc]
                if target_piece is None or target_piece.color != self.color:
                    moves.append((row + dr, col + dc))
        return moves


class Pawn(Piece):
    def __str__(self):
        return 'P' if self.color == 'white' else 'p'

    def get_moves(self, board, row, col):
        moves = []
        direction = -1 if self.color == 'white' else 1
        start_row = 6 if self.color == 'white' else 1

        if 0 <= row + direction < 8 and board[row + direction][col] is None:
            moves.append((row + direction, col))
            if row == start_row and board[row + 2 * direction][col] is None:
                moves.append((row + 2 * direction, col))

        for dc in [-1, 1]:
            if 0 <= row + direction < 8 and 0 <= col + dc < 8:
                target_piece = board[row + direction][col + dc]
                if target_piece is not None and target_piece.color != self.color:
                    moves.append((row + direction, col + dc))
        return moves


def create_board():
    board = [[None] * 8 for _ in range(8)]

    for col in range(8):
        board[1][col] = Pawn('black')
        board[6][col] = Pawn('white')

    pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    for i, piece in enumerate(pieces):
        board[0][i] = piece('black')
        board[7][i] = piece('white')

    return board


def print_board(board):
    print("   a b c d e f g h")
    print(" +-----------------+")
    for i in range(8):
        print(f"{8-i}|", end=" ")
        for j in range(8):
            piece = board[i][j]
            print(piece if piece else '.', end=' ')
        print(f"|{8-i}")
    print(" +-----------------+")
    print("   a b c d e f g h")


def parse_position(pos):
    col, row = pos
    return 8 - int(row), ord(col) - ord('a')


def get_all_moves(board, color):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece is not None and piece.color == color:
                for move in piece.get_moves(board, row, col):
                    moves.append(((row, col), move))
    return moves


def get_capturing_moves(board, color):
    capturing_moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece is not None and piece.color == color:
                for move in piece.get_moves(board, row, col):
                    target_row, target_col = move
                    if piece.is_capturing_move(board, row, col, target_row, target_col):
                        capturing_moves.append(((row, col), move))
    return capturing_moves


def is_valid_move(board, move, color):
    start, end = move
    start_row, start_col = parse_position(start)
    end_row, end_col = parse_position(end)
    piece = board[start_row][start_col]
    if piece is None or piece.color != color:
        return False, "No piece of your color at the starting position."

    capturing_moves = get_capturing_moves(board, color)
    if capturing_moves:
        if ((start_row, start_col), (end_row, end_col)) not in capturing_moves:
            return False, "You must make a capturing move if available."
    else:
        if (end_row, end_col) not in piece.get_moves(board, start_row, start_col):
            return False, "Illegal move for the piece."

    return True, None


def make_move(board, move):
    start, end = move
    start_row, start_col = parse_position(start)
    end_row, end_col = parse_position(end)
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = None


def reverse_move(board, move, captured_piece):
    start, end = move
    start_row, start_col = parse_position(start)
    end_row, end_col = parse_position(end)
    board[start_row][start_col] = board[end_row][end_col]
    board[end_row][end_col] = captured_piece


def is_checkmate(board, color):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece is not None and piece.color == color:
                if piece.get_moves(board, row, col):
                    return False
    return True


def main():
    board = create_board()
    current_player = 'white'
    move_history = []
    while True:
        print_board(board)
        print(f"{current_player.capitalize()}'s turn.")
        move_input = input("Enter your move (e.g., 'e2 e4'), 'display' to show the board, 'undo' to reverse your last move, or 'quit' to exit: ").strip()

        if move_input.lower() == 'display':
            print_board(board)
            continue

        if move_input.lower() == 'quit':
            print(f"{current_player.capitalize()} quits. {('White' if current_player == 'black' else 'Black')} wins!")
            break

        if move_input.lower() == 'undo':
            if not move_history:
                print("No moves to undo.")
                continue

            last_move, captured_piece = move_history.pop()
            reverse_move(board, last_move, captured_piece)
            current_player = 'white' if current_player == 'black' else 'black'
            continue

        try:
            start, end = move_input.split()
        except ValueError:
            print("Invalid input format. Please enter the move in 'e2 e4' format.")
            continue

        is_valid, error_message = is_valid_move(board, (start, end), current_player)
        if not is_valid:
            print(error_message)
            continue

        # Store the current state to enable undo
        start_row, start_col = parse_position(start)
        end_row, end_col = parse_position(end)
        captured_piece = board[end_row][end_col]
        move_history.append(((start_row, start_col), captured_piece))

        make_move(board, (start, end))
        if is_checkmate(board, 'white' if current_player == 'black' else 'black'):
            print_board(board)
            print(f"Checkmate! {current_player.capitalize()} wins!")
            break

        current_player = 'black' if current_player == 'white' else 'white'


if __name__ == "__main__":
    main()