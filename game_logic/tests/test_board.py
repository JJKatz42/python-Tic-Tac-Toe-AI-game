import pytest as pytest

from game_logic import board as board, player as player


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


@pytest.mark.parametrize("move", range(0, 9))
def test_board_check_move_negative(move):
    test_board = board.Board("X", "O")
    test_board.moves_made += str(move)
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
    test_board1.moves_made += str(test_move)
    test_player = player.Player("X")
    assert test_board1.apply_move(test_move, test_player) == False
    assert test_board1.board_list[test_move] == " "
    assert str(test_move) in test_board1.moves_made


def test_board_unapply_move():
    test_board = board.Board("X", "O")
    test_move = 3
    test_board.moves_made += str(test_move)
    test_board.board_list[test_move] = "X"
    test_board.unapply_move(test_move)
    assert test_board.board_list[test_move] == " "
    assert str(test_move) not in test_board.moves_made


def test_board_check_win_for_player_positive():
    test_board = board.Board("X", "O")
    test_player = player.Player("X")
    test_board.board_list = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert test_board.check_win_for_player(test_player)


def test_board_check_win_for_player_negative():
    test_board = board.Board("X", "O")
    test_player = player.Player("X")
    test_board.board_list = ["X", "X", " ", " ", " ", " ", " ", " ", " "]
    assert not test_board.check_win_for_player(test_player)


def test_board_check_for_tie():
    test_player = player.Player("X")
    test_board = board.Board(test_player, "O")
    test_board.board_list = ["X", "X", "O", "O", "O", "X", "X", "O", "X"]
    assert test_board.check_for_tie()


def test_board_reset():
    test_board = board.Board("X", "O")
    test_board.board_list = ["X", " ", " ", " ", "O", " ", " ", " ", " "]
    test_board.moves_made = "1237"
    test_board.reset()
    assert test_board.board_list == [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    assert test_board.moves_made == ""


def test_board_get_possible_moves():
    test_board = board.Board("X", "O")
    test_board.board_list = ["X", " ", " ", " ", " ", " ", "X", " ", "O"]
    assert test_board.get_possible_moves() == [1, 2, 3, 4, 5, 7]









