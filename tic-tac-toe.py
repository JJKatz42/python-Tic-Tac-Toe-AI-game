import board as board
import player as base_player
import rand_player as rand_player
import AI_player as AI_player

        
def construct_player_for(marker):
    choice = base_player.Player.get_choice(marker)
    if choice == "human":
        player = base_player.Player(marker)
    if choice == "CPU":
        depth = AI_player.AIPlayer.get_depth()
        player = AI_player.AIPlayer(marker, depth)
    if choice == "random":
        player = rand_player.RandomPlayer(marker)
    return player


def main():
    player1 = construct_player_for("X")
    player2 = construct_player_for("O")
    game_board = board.Board(current_player=player1, other_player=player2)
    while game_board.check_game_over(player1=player1, player2=player2) == False:
        print(game_board)
        game_board.draw_board()
        move = game_board.current_player.get_move(board=game_board)
        game_board.apply_move(move, game_board.current_player)
        game_board.turn_player()
    game_board.turn_player()
    print("=========================")
    game_board.draw_board()
    if game_board.check_win_for_player(game_board.current_player):
        print(f"congrats player {game_board.current_player.marker} won")
    elif game_board.check_win_for_player(game_board.other_player):
        print(f"congrats player {game_board.other_player.marker} won")
    else:
        print("It was a tie you both loose.")


if __name__ == "__main__":
    main()
