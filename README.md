# Tic-Tac-Toe-AI.py

## Architexture
There are two main classes in the basic game
 - Board class
 - Player class
 Then there is the main game logic which goes into tic-tac-toe
 
 The PLayer class has two sub classes
  - AIPlayer
  - RandPlayer
  
  _These are additional add ons, if they are not wanted there are some print statements that need to be changed_
  
  ## Differences in the player classes
  The two sublcasses of Player that are used in the game only overide one function from the parent class: 
   The get_move() function
  what changes between the Player classes is that:
   ### In the normal Player
   - there is a human player and there is an input prompt to ask for the move
   - there is a is_valid() funtion which checks if the input was valid (1-9 + not a taken move)
   (here's where it gets intresting)
   ### In the AIPlayer
   - there is a minimax function
    - the maximize funtion is called to find the best move possible
    - to find the best move possible the AI player has to calculate what the opponent will do and how to counteract it
    - 
