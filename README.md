# Tic-Tac-Toe-AI.py

## Architecture
There are two main classes in the basic game
 - Board class
 - Player class
 
 The PLayer class has two subclasses
  - AIPlayer
  - RandPlayer
  
  _These are additional add ons, if they are not wanted there are some print statements that need to be changed_
  
  ## Differences in the player classes
  The two subclasses of Player that are used in the game only override one function from the parent class: 
   The get_move() function
  
  what changes between the Player classes is that:
   ### In the normal Player
   - there is a human player and there is an input prompt to ask for the move
   - there is an is_valid() function which checks if the input was valid (1-9 + not a taken move)
   
   (here's where it gets interesting)
   ### In the AIPlayer
   - there is a minimax algorithm 
   - the maximize function is called to find the best move possible
   - to find the best move possible the AI player has to calculate what the opponent will do and how to counteract it
   - that is where the minimize() function comes in, which finds the move the opponent will make to minimize the AI players next move
   - There are two parameters that go into the maximize and minimize functions
   1. The board, which is needed to get functions and parameters from the board class
   2. The depth, which is used as the number of turns the AI player can look ahead
   ![alt text](https://upload.wikimedia.org/wikipedia/commons/1/1f/Tic-tac-toe-full-game-tree-x-rational.jpg "Tic-tac_toe gameboard")
   - The maximize and minimize functions use the claculate_score() function to find which of the possible moves is the best move and that move is sent back up and returned as the best_move, which then flows back into the regular player code
   
   (Now the simple one)
   ### In the RandPlayer
   - there is one function and that is the override of the get_move()
   - random is imported, which is used to randomly choose one of the possible moves 
   - That is the extent of a random player
## Win method
 - At the moment the win method is hardcoded, as there are a list of lists that have all the possible win combinations
 - the way the win is checked, is by checking if there is only one type of marker (X or O) in all three of the spaces of one of the possible win combinations  

