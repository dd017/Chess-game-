class ChessBoard:
    def __init__(self, skin='classic'):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.skin = skin
        self.setup_pieces()

    def setup_pieces(self):
        piece_classes = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece_class in enumerate(piece_classes):
            self.board[0][i] = piece_class('white', self.skin)
            self.board[7][i] = piece_class('black', self.skin)
        for i in range(8):
            self.board[1][i] = Pawn('white', self.skin)
            self.board[6][i] = Pawn('black', self.skin)

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

class ChessPiece:
    SYMBOLS = {
        'classic': {
            'pawn': '♙♟', 'rook': '♖♜', 'knight': '♘♞', 'bishop': '♗♝',
            'queen': '♕♛', 'king': '♔♚'
        },
        'modern': {
            'pawn': 'Pp', 'rook': 'Rr', 'knight': 'Nn', 'bishop': 'Bb',
            'queen': 'Qq', 'king': 'Kk'
        },
        'fancy': {
            'pawn': '⚜⚛', 'rook': '🏰🏯', 'knight': '♞♘', 'bishop': '✝✙',
            'queen': '👑♕', 'king': '♔♚'
        }
    }

    def __init__(self, color, name, skin='classic'):
        self.color = color
        self.name = name
        self.skin = skin

    def __str__(self):
        symbols = self.SYMBOLS[self.skin]
        return symbols[self.name][0] if self.color == 'white' else symbols[self.name][1]

class Pawn(ChessPiece):
    def __init__(self, color, skin='classic'):
        super().__init__(color, 'pawn', skin)

class Rook(ChessPiece):
    def __init__(self, color, skin='classic'):
        super().__init__(color, 'rook', skin)

class Knight(ChessPiece):
    def __init__(self, color, skin='classic'):
        super().__init__(color, 'knight', skin)

class Bishop(ChessPiece):
    def __init__(self, color, skin='classic'):
        super().__init__(color, 'bishop', skin)

class Queen(ChessPiece):
    def __init__(self, color, skin='classic'):
        super().__init__(color, 'queen', skin)

class King(ChessPiece):
    def __init__(self, color, skin='classic'):
        super().__init__(color, 'king', skin)
class ChessGame:
    def __init__(self, difficulty='easy', skin='classic'):
        self.board = ChessBoard(skin=skin)
        self.current_player = 'white'
        self.difficulty = difficulty


    def play(self):
        while True:
            self.board.print_board()
            if self.current_player == 'white':
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
            else:
                print("AI is thinking...")
                ai_move = self.ai_move()
                if ai_move:
                    self.move_piece(*ai_move)
                else:
                    print("AI has no valid moves, switching to player.")
                    self.current_player = 'white'

if __name__ == "__main__":
    difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    skin = input("Select board skin (classic, modern, fancy): ").lower()
    game = ChessGame(difficulty=difficulty, skin=skin)
    game.play()
