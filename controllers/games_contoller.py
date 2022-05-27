from flask import Flask, redirect, render_template, request
from repositories import developer_repository
from repositories import game_repository
from models.game import Game

from flask import Blueprint

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", all_games = games)