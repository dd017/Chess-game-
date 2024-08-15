import random

class ChessGame:
    def __init__(self, difficulty='easy'):
        self.board = ChessBoard()
        self.current_player = 'white'
        self.difficulty = difficulty
    
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
    
    def ai_move(self):
        possible_moves = self.get_all_moves('black')
        
        if self.difficulty == 'easy':
            return random.choice(possible_moves)
        elif self.difficulty == 'medium':
            return self.medium_ai(possible_moves)
        elif self.difficulty == 'hard':
            return self.hard_ai(possible_moves)
    
    def medium_ai(self, possible_moves):
        # Basic strategy: prefer capturing moves
        best_move = None
        for move in possible_moves:
            from_pos, to_pos = move
            from_row, from_col = 8 - int(from_pos[1]), ord(from_pos[0]) - ord('a')
            to_row, to_col = 8 - int(to_pos[1]), ord(to_pos[0]) - ord('a')
            if self.board.board[to_row][to_col] is not None:  # capturing a piece
                best_move = move
                break
        return best_move if best_move else random.choice(possible_moves)
    
    def hard_ai(self, possible_moves):
        # Advanced AI (e.g., Minimax algorithm can be added here)
        # For simplicity, we'll still use a basic evaluation for now.
        return self.medium_ai(possible_moves)
    
    def get_all_moves(self, color):
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board.board[row][col]
                if piece is not None and piece.color == color:
                    valid_moves = piece.valid_moves(self.board, row, col)
                    for move in valid_moves:
                        moves.append((f"{chr(col + ord('a'))}{8 - row}", f"{chr(move[1] + ord('a'))}{8 - move[0]}"))
        return moves

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
    game = ChessGame(difficulty=difficulty)
    game.play()
