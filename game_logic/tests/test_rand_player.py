import pytest as pytest


from game_logic import board as board, rand_player as rand_player, player as player


def test_rand_player_get_move():
    test_board = board.Board("X", "O")
    test_board.board_list = [" ", "X", "X", "X", "X", " ", "X", " ", "X"]
    test_player = player.Player("X")
    test_rand_player = rand_player.RandomPlayer(test_player)
    assert test_rand_player.get_move(test_board) in test_board.get_possible_moves()
