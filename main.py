class ChessGame:
    def __init__(self, skin='classic'):
        self.board = ChessBoard(skin=skin)
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
    skin = input("Select board skin (classic, modern, fancy): ").lower()
    game = ChessGame(skin=skin)
    game.play()
