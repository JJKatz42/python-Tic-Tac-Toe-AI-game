import player
import random


class RandomPlayer(player.Player):
    def get_move(self, board):
        possible_moves = board.get_possible_moves()
        return random.choice(possible_moves)
