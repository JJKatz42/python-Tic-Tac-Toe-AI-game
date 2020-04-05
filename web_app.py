from flask import Flask, session, redirect, url_for
from flask import render_template
from flask_session import Session

from game_logic.board import Board
from game_logic.player import Player


# creates a Flask application, named app
app = Flask(__name__)
SESSION_TYPE = "redis"
app.config.from_object(__name__)
Session(app)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def game_handler():
    if "board" not in session:
        player1 = Player(marker="X")
        player2 = Player(marker="O")
        game_board = Board(player1, player2)
        session["game_board"] = game_board
    else:
        game_board = session["game_board"]
    if game_board.check_for_tie():
        print("There is a TIE")
        session["tie"] = True
    elif game_board.check_game_over():
        print(f"player {game_board.current_player.marker} has won")
        session["winner_found"] = True
    else:
        game_board.turn_player()
    return render_template("index.html",
                           game_board=game_board,
                           turn=game_board.current_player.marker,
                           winner_found=session.get("winner_found", False),
                           tie=session.get("tie", False))


@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    move = 3*row + col
    game_board: Board = session["game_board"]
    game_board.apply_move(move)

    return redirect(url_for("game_handler"))


@app.route("/reset")
def reset():
    session.pop("game_board")
    session.pop("tie")
    session.pop("winner_found")
    return redirect(url_for("game_handler"))