class ChessPiece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"{self.color[0]}{self.name[0].upper()}"

    def valid_moves(self, board, row, col):

        pass

class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'pawn')

    def valid_moves(self, board, row, col):

        moves = []
        direction = 1 if self.color == 'white' else -1


        if 0 <= row + direction < 8 and board.board[row + direction][col] == ' ':
            moves.append((row + direction, col))

            if (self.color == 'white' and row == 6) or (self.color == 'black' and row == 1):
                if board.board[row + 2 * direction][col] == ' ':
                    moves.append((row + 2 * direction, col))


        for dc in [-1, 1]:
            if 0 <= col + dc < 8 and 0 <= row + direction < 8:
                target = board.board[row + direction][col + dc]
                if target != ' ' and target.color != self.color:
                    moves.append((row + direction, col + dc))
        return moves

class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'rook')

    def valid_moves(self, board, row, col):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            r, c = row, col
            while True:
                r += dr
                c += dc
                if 0 <= r < 8 and 0 <= c < 8:
                    target = board.board[r][c]
                    if target == ' ':
                        moves.append((r, c))
                    elif target.color != self.color:
                        moves.append((r, c))
                        break
                    else:
                        break
                else:
                    break
        return moves
class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        self.board[0] = [
            Rook('white'), Knight('white'), Bishop('white'),
            Queen('white'), King('white'), Bishop('white'),
            Knight('white'), Rook('white')
        ]
        self.board[1] = [Pawn('white') for _ in range(8)]

        self.board[7] = [
            Rook('black'), Knight('black'), Bishop('black'),
            Queen('black'), King('black'), Bishop('black'),
            Knight('black'), Rook('black')
        ]
        self.board[6] = [Pawn('black') for _ in range(8)]

    def print_board(self):
        print("  a b c d e f g h")
        print(" +-----------------+")
        for row in range(8):
            print(f"{8 - row}|", end=" ")
            for col in range(8):
                piece = self.board[row][col]
                print(str(piece) if piece else ' ', end=' ')
            print(f"|{8 - row}")
        print(" +-----------------+")
        print("  a b c d e f g h")

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = 'white'

    def move_piece(self, from_pos, to_pos):
        from_row, from_col = 8 - int(from_pos[1]), ord(from_pos[0]) - ord('a')
        to_row, to_col = 8 - int(to_pos[1]), ord(to_pos[0]) - ord('a')

        piece = self.board.board[from_row][from_col]
        if piece is None or piece.color != self.current_player:
            print("Invalid move: No piece of yours at this position.")
            return False

        if (to_row, to_col) not in piece.valid_moves(self.board, from_row, from_col):
            print("Invalid move: Piece cannot move to this position.")
            return False

        self.board.board[to_row][to_col] = piece
        self.board.board[from_row][from_col] = None
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        return True

    def play(self):
        while True:
            self.board.print_board()
            print(f"{self.current_player.capitalize()}'s turn")
            move = input("Enter your move (e.g., e2 e4): ")
            try:
                from_pos, to_pos = move.split()
                if len(from_pos) == 2 and len(to_pos) == 2:
                    if self.move_piece(from_pos, to_pos):
                        continue
            except ValueError:
                pass
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    game = ChessGame()
    game.play()

