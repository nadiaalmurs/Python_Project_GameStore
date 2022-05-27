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

@games_blueprint.route("/games/<id>/delete", methods=['POST'])
def delete_game(id):
    game_repository.delete(id)
    return redirect("/games")

@games_blueprint.route("/games/new", methods=['GET'])
def new_game():
    games = game_repository.select_all()
    return render_template("games/new.html", all_games = games)

@games_blueprint.route("/games", methods=['POST'])
def create_game():
    title = request.form['title']
    developer_id = request.form['developer']
    genre = request.form['genre']
    description = request.form['description']
    stock = request.form['stock']
    buy = request.form['buy']
    sell = request.form['sel']

    developer = developer_repository.select(developer_id)

    game = Game(title, genre, description, stock, buy, sell, developer)

    game_repository.save(game)
    return redirect("/games")