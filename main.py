class ChessPiece:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    
    def __str__(self):
        return f"{self.color[0]}{self.name[0].upper()}"

class ChessBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        self.board[0] = [
            ChessPiece('white', 'rook'), ChessPiece('white', 'knight'), ChessPiece('white', 'bishop'),
            ChessPiece('white', 'queen'), ChessPiece('white', 'king'), ChessPiece('white', 'bishop'),
            ChessPiece('white', 'knight'), ChessPiece('white', 'rook')
        ]
        self.board[1] = [ChessPiece('white', 'pawn') for _ in range(8)]

        self.board[7] = [
            ChessPiece('black', 'rook'), ChessPiece('black', 'knight'), ChessPiece('black', 'bishop'),
            ChessPiece('black', 'queen'), ChessPiece('black', 'king'), ChessPiece('black', 'bishop'),
            ChessPiece('black', 'knight'), ChessPiece('black', 'rook')
        ]
        self.board[6] = [ChessPiece('black', 'pawn') for _ in range(8)]
    
    def print_board(self):
        print("  a b c d e f g h")
        print(" +-----------------+")
        for row in range(8):
            print(f"{8 - row}|", end=" ")
            for col in range(8):
                piece = self.board[row][col]
                print(str(piece) if piece != ' ' else ' ', end=' ')
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
        
        if piece == ' ' or piece.color != self.current_player:
            print("Invalid move: No piece of yours at this position.")
            return False

        if self.board.board[to_row][to_col] != ' ' and self.board.board[to_row][to_col].color == self.current_player:
            print("Invalid move: You can't capture your own piece.")
            return False

        self.board.board[to_row][to_col] = piece
        self.board.board[from_row][from_col] = ' '
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

