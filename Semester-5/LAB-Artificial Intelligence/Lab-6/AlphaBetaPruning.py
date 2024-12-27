class AlphaBetaPruning:
    def __init__(self, depth, game_state, player):
        self.depth = depth
        self.game_state = game_state
        self.player = player  # 'X' for maximizer, 'O' for minimizer
        self.nodes_evaluated = 0

    def is_terminal(self, state):

        return check_winner(state, 'X') or check_winner(state, 'O') or is_draw(state)

    def utility(self, state):
        if check_winner(state, 'X'):
            return 1
        elif check_winner(state, 'O'):
            return -1
        return 0

    def alphabeta(self, state, depth, alpha, beta, maximizing_player):
        self.nodes_evaluated += 1  # Count the node being evaluated
        if depth == 0 or self.is_terminal(state):
            return self.utility(state)

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(9):
                if state[i] == ' ':
                    state[i] = 'X'
                    eval = self.alphabeta(state, depth - 1, alpha, beta, False)
                    state[i] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta cut-off
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(9):
                if state[i] == ' ':
                    state[i] = 'O'
                    eval = self.alphabeta(state, depth - 1, alpha, beta, True)
                    state[i] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha cut-off
            return min_eval

    def best_move(self, state):
        best_value = float('-inf')
        move = None
        for i in range(9):
            if state[i] == ' ':
                state[i] = 'X'
                move_value = self.alphabeta(state, self.depth, float('-inf'), float('inf'), False)
                state[i] = ' '
                if move_value > best_value:
                    best_value = move_value
                    move = i
        return move

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                      (0, 4, 8), (2, 4, 6)]  
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_draw(board):
    return ' ' not in board  

def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def play_tic_tac_toe():
    board = [' '] * 9
    ai = AlphaBetaPruning(depth=4, game_state=board, player='X')
    
    while True:
        print_board(board)
        move = int(input("Enter your move (0-8): "))
        
        if board[move] != ' ':
            print("Invalid move, try again.")
            continue
        board[move] = 'O'
        
        if ai.is_terminal(board):
            if check_winner(board, 'O'):
                print("You win!")
            elif is_draw(board):
                print("It's a draw!")
            break
        
        ai_move = ai.best_move(board)
        board[ai_move] = 'X'
        print("AI chose position", ai_move)

        if ai.is_terminal(board):
            if check_winner(board, 'X'):
                print("AI wins!")
            elif is_draw(board):
                print("It's a draw!")
            break

        # Displaying the number of nodes evaluated for this move
        print(f"Nodes evaluated by AI for this move: {ai.nodes_evaluated}")
        ai.nodes_evaluated = 0  # Reset node counter for the next move

play_tic_tac_toe()
