import pytest as pytest
import unittest.mock as mock

from game_logic import board as board, player as player


def test_player_initialization():
    test_player = player.Player("X")
    assert test_player.marker == "X"


def test_player_is_valid_move_positive():
    test_board = board.Board("X", "O")
    test_player = player.Player("X")
    move = 3
    assert test_player.is_valid_move(move=move, board=test_board)


def test_player_is_valid_move_negative():
    test_board = board.Board("X", "O")
    test_player = player.Player("X")
    move = 20
    assert not test_player.is_valid_move(move=move, board=test_board)


def test_player_get_move_positive():
    test_player = player.Player('X')
    test_board = board.Board(test_player, "O")
    with mock.patch('builtins.input', return_value='3'):
        assert test_player.get_move(test_board) == 2


def test_player_get_move_negative():
    test_player = player.Player('X')
    test_board = board.Board(test_player, "O")
    with mock.patch('builtins.input', return_value='3'):
        assert not test_player.get_move(test_board) == 1


def test_player_get_choice():
    test_player = player.Player('X')
    with mock.patch('builtins.input', return_value='human'):
        assert test_player.get_choice("X") == 'human'


def test_player_validate_choice_positive():
    test_player = player.Player("X")
    choice = "human"
    assert test_player.validate_choice(choice=choice)


def test_player_validate_choice_negative():
    test_player = player.Player("X")
    choice = "ahsdbasjkd"
    assert not test_player.validate_choice(choice=choice)