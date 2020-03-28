import player
import board



class AIPlayer(player.Player):
    max_depth = 9
    def __init__(self, marker, max_depth):
        self.max_depth = max_depth
        super().__init__(marker)
    

    def opp_player(self):
        if self.marker == "X":
            opp_marker = "O"
        elif self.marker == "O":
            opp_marker = "X"
        return opp_marker


    def get_move(self, board):
        (best_move, _) = self.maximize(board, 0)
        return int(best_move)

    def calculate_score(self, board):
        # move = int(board.moves_made[-1])
        # score = 0
        # for line in board.win_combinations:
        #     if move in line:
        #         line_score = 0
        #         board_line = [board.board_list[i] for i in line]
        #         if board_line.count(self.marker) == 3:
        #             line_score = 10

        #         elif board_line.count(self.opp_player) == 2:
        #             line_score = 5

        #         elif board_line.count(self.marker) == 2 and board_line.count(" ") == 1:
        #             line_score = 2
                
        #         elif board_line.count(self.marker) == 1 and board_line.count(" ") == 2:
        #             line_score = 1
        #         score+=line_score
        # return score
        if board.check_win_for_player(self):
            return 1
        elif board.check_win_for_player(player.Player(self.opp_player())):
            return -1
        else:
            return 0

    def is_terminal(self, board):
        return board.check_game_over(self, player.Player(self.opp_player()))

    
    
    def maximize(self, board, depth):
        if self.is_terminal(board) or depth == self.max_depth:
            # in case of terminal case
            return None, self.calculate_score(board)
        max_score = -10000000
        best_move = None
        for possible_move in board.get_possible_moves():
            board.apply_move(possible_move, self)
            (_, score) = self.minimize(board, depth+1)
            board.unapply_move(possible_move)
            if score > max_score:
                max_score = score
                best_move = possible_move
        return best_move, max_score

    
    def minimize(self, board, depth):
        if self.is_terminal(board) or depth == self.max_depth:
            # in case of terminal case
            return None, self.calculate_score(board)
        min_score = 10000000
        worst_move = None
        for possible_move in board.get_possible_moves():
            board.apply_move(possible_move, player.Player(self.opp_player()))
            (_, score) = self.maximize(board, depth)
            board.unapply_move(possible_move)
            if score < min_score:
                min_score = score
                worst_move = possible_move
        return worst_move, min_score


    @classmethod
    def get_depth(cls):
        depth=""
        have_depth = False
        while have_depth == False:
            depth = input("What would you like the AI's lookahead to be? (1-9)\n==> ")
            try:
                if int(depth) in range(1, 10):
                    have_depth = True
                else:
                    print("That is not a valid choice, please try again")
            except(ValueError,TypeError):
                print("That is not a valid choice, please try again")
        return int(depth)