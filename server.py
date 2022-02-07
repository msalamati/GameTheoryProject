from flask import Flask, request, render_template
import pygambit


app = Flask(__name__)


@app.route("/solve/01", methods=["POST"])
def solve():
    num_of_months = float(request.form.get("num_of_months"))
    soldier_income = float(request.form.get("soldier_income"))
    normal_income = float(request.form.get("normal_income"))
    num_of_soldiers = float(request.form.get("num_of_soldiers"))

    file = open("static/files/01.efg")

    game_rep = file.read().format(
        - num_of_months * soldier_income * num_of_soldiers,
        num_of_months * soldier_income,
        - num_of_months * soldier_income * num_of_soldiers,
        num_of_months * soldier_income,
        - num_of_months * normal_income * num_of_soldiers,
        num_of_months * normal_income,
    )

    game = pygambit.Game.parse_game(game_rep)
    nash_eq = pygambit.nash.lcp_solve(game, use_strategic=True, rational=False)

    return render_template("result.html", result=str(nash_eq))


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")
