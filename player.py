
class Player:
    marker = "X"


    def __init__(self, marker):
        self.marker = marker


    @staticmethod
    def safe_to_integer(value,default =-1):
        try:
            return int(value)
        except(ValueError,TypeError):
            return default


    @staticmethod
    def is_valid_move(move, board):
        if Player.safe_to_integer(move) not in range(1,10):
            return False
        move = int(move)-1
        return board.check_move(move)


    def get_move(self, board):
        move=""
        while self.is_valid_move(move, board) == False:
            move = input(f"What move would you like to make {self.marker}, (1-9) \n==> ")
            if self.is_valid_move(move, board) == False:
                print("Sorry please give a value from 1-9 that is not taken, try again")
        return int(move)-1   

    @classmethod
    def get_choice(cls, marker):
        choice=""
        choice_made = False
        while choice_made == False:
            choice = input(f"what would you like player {marker} to play as human, CPU, or random? \n ==> ")
            choice_made = Player.validate_choice(choice)
        return choice
    
    
    @classmethod   
    def validate_choice(cls, choice):
        if choice == "human":
            return True
        elif choice == "CPU":
            return True
        elif choice == "random":
            return True
        else:
            print("Sorry that wasn't one of the choices, try again")
            return False
            
        

