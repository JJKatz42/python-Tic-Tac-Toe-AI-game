from flask import Flask, session, redirect, url_for, abort, Response
from flask import render_template, request
from flask_session import Session

from game_logic.board import Board
from game_logic.player import Player
from game_logic.AI_player import AIPlayer
from game_logic.rand_player import RandomPlayer


# creates a Flask application, named app
app = Flask(__name__)
SESSION_TYPE = "redis"
SESSION_PERMANENT = False

app.config.from_object(__name__)
Session(app)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def start_game_handler():
    return render_template("start_game.html")


@app.route("/result", methods=['POST'])
def result_handler():
    result = request.form
    session.pop("game_board", None)
    session.pop("tie", None)
    session.pop("winner_found", None)
    player1 = None
    player2 = None
    if "player1_type" not in result or "player2_type" not in result:
        abort(Response('I send it back!'))
    if result["player1_type"] == "human":
        player1 = Player(marker="X")
    elif result["player1_type"] == "CPU":
        player1 = AIPlayer(marker="X", max_depth=int(result["CPU_lookahead1"]))
    elif result["player1_type"] == "random":
        player1 = AIPlayer(marker="X")
    if result["player2_type"] == "human":
        player2 = Player(marker="O")
    elif result["player2_type"] == "CPU":
        player2 = AIPlayer(marker="O", max_depth=int(result["CPU_lookahead1"]))
    elif result["player2_type"] == "random":
        player2 = RandomPlayer(marker="O")
    game_board = Board(player1, player2)
    session["game_board"] = game_board

    return redirect(url_for("game_handler"))


@app.route("/game")
def game_handler():
    game_board = session["game_board"]
    if game_board.check_for_tie():
        print("There is a TIE")
        session["tie"] = True
    elif game_board.check_game_over():
        game_board.turn_player()
        print(f"player {game_board.current_player.marker} has won")
        session["winner_found"] = True

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
    game_board.turn_player()

    return redirect(url_for("game_handler"))


@app.route("/reset")
def reset():
    session.pop("game_board", None)
    session.pop("tie", None)
    session.pop("winner_found", None)
    return redirect(url_for("game_handler"))