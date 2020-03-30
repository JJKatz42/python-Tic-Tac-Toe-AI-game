import pytest as pytest

import board as board
import player as player



def test_board_initialization():
    test_board = board.Board("X", "O")
    assert test_board.current_player == "X"
    assert test_board.other_player == "O"


def test_board_repr():
    test_board = board.Board("X", "O")
    assert test_board.__repr__() == test_board.instruction_board



def test_board_turn_player():
    test_board = board.Board("X", "O")
    test_board.turn_player()
    assert test_board.current_player == "O"
    assert test_board.other_player == "X"


@pytest.mark.parametrize("move", range(0,9))
def test_board_check_move_negative(move):
    test_board = board.Board("X", "O")
    test_board.moves_made+=str(move)
    assert test_board.check_move(move) == False


def test_board_check_move_positive():
    test_board = board.Board("X", "O")
    assert test_board.check_move(2) == True


def test_board_apply_move_positive():
    test_board = board.Board("X", "O")
    test_move = 5
    test_player = player.Player("X")
    assert test_board.apply_move(test_move, test_player)
    assert test_board.board_list[test_move] == test_player.marker
    assert str(test_move) in test_board.moves_made


def test_board_apply_move_negative():
    test_board1 = board.Board("X", "O")
    test_move = 4
    test_board1.moves_made+=str(test_move)
    test_player = player.Player("X")
    assert test_board1.apply_move(test_move, test_player) == False
    assert test_board1.board_list[test_move] == " "
    assert str(test_move) in test_board1.moves_made


