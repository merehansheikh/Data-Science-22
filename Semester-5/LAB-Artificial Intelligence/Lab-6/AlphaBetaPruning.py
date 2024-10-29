class AlphaBetaPruning: 
    def __init__(self, depth, game_state, player):
        self.depth = depth
        self.game_state = game_state
        self.player = player

    def is_terminal(self, state):
        pass

    def is_draw(state)
        if ' ' not in board:
            return True
        return False
    
    def check_winner(board, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                      (0, 4, 8), (2, 4, 6)]
        for i in win_conditions:
            