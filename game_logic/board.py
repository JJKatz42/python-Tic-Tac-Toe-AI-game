class Board:
    board = """
  {0}  |  {1}  |  {2}
  ---+-----+---
  {3}  |  {4}  |  {5}
  ---+-----+---
  {6}  |  {7}  |  {8}"""

    win_combinations = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 5, 8], [3, 4, 5], [6, 7, 8], [2, 4, 6]]
    current_player = None
    other_player = None
    instruction_board = "\n1  |  2  |  3\n---+-----+---\n4  |  5  |  6\n---+-----+---\n7  |  8  |  9"

    def __init__(self, current_player, other_player):
        self.board_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.current_player = current_player
        self.other_player = other_player
        self.moves_made = ""

    def __repr__(self):
        ''' returns a string representation of a Board '''
        return self.instruction_board

    def draw_board(self):
        print(self.board.format(*self.board_list))

    def turn_player(self):
        temp = self.current_player
        self.current_player = self.other_player
        self.other_player = temp

    def check_move(self, move):
        """"checks if the move made by the player is valid
        
            args:
                move (int): 0-8 move an the board
            
            returns: 
                bool: false, if not a good int or move already made. false, else
        """

        if str(move) in self.moves_made:
            return False
        return True

    def apply_move(self, move):
        """updates the board_list with the move made by the player
        
            args:
                player (str): X or O
                move (int): 0-8 move an the board
            
            returns: 
                bool: true, if there was a succesful move made. false, else
        """
        if self.check_move(move=move):
            self.board_list[move] = self.current_player.marker  # changes value in the board to player which is either X or O
            self.moves_made += str(move)  # keeps track of all moves
            return True
        else:
            return False

    def unapply_move(self, move):
        self.board_list[move] = " "
        self.moves_made = self.moves_made[:-1]

    def check_win_for_player(self, player):
        for wins in self.win_combinations:
            if player.marker == self.board_list[wins[0]] == self.board_list[wins[1]] == self.board_list[wins[2]]:  # checks for each value in each list is equally to the same thing (X or O)
                return True
        return False

    def check_for_tie(self):
        if " " not in self.board_list and not self.check_win_for_player(self.current_player) and not self.check_win_for_player(self.other_player):
            # if there are no spaces and here is new win it has to be a tie
            return True

    def check_game_over(self):
        if (self.check_win_for_player(self.current_player) or
                self.check_win_for_player(self.other_player) or
                self.check_for_tie()):
            return True
        return False

    def reset(self):
        self.board_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.moves_made = ""

    def get_possible_moves(self):
        possible_moves = []
        for i in range(len(self.board_list)):
            if self.board_list[i] == " ":
                possible_moves.append(i)
        return possible_moves

    def check_empty(self):
        if "X" in self.board_list or "O" in self.board_list:
            return False
        return True
