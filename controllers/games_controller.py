from crypt import methods
from flask import Flask, redirect, render_template, request
from models import developer
from repositories import developer_repository
from repositories import game_repository
from models.game import Game
from models.developer import Developer

from flask import Blueprint

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    genres = game_repository.get_genres()
    developers = developer_repository.select_all()
    return render_template("games/index.html", all_games = games, genres=genres, developers=developers)

@games_blueprint.route("/games/<id>/delete", methods=['POST'])
def delete_game(id):
    game_repository.delete(id)
    return redirect("/games")

@games_blueprint.route("/games/new", methods=['GET'])
def new_game():
    games = game_repository.select_all()
    developers = developer_repository.select_all()
    active_developers = []
    for developer in developers:
        if developer.active == True:
            active_developers.append(developer) 
    return render_template("games/new.html", all_games = games, all_developers = active_developers)

@games_blueprint.route("/games", methods=['POST'])
def create_game():
    title = request.form['title']
    developer_id = request.form['developer_id']
    genre = request.form['genre']
    description = request.form['description']
    stock = request.form['stock']
    buy = request.form['buy']
    sell = request.form['sell']

    developer = developer_repository.select(developer_id)

    game = Game(title, genre, description, stock, buy, sell, developer)

    game_repository.save(game)
    return redirect("/games")

@games_blueprint.route("/games/<id>", methods=['GET'])
def show_game(id):
    game = game_repository.select(id)
    return render_template('games/show.html', game = game)

@games_blueprint.route("/games/<id>/edit", methods=['GET'])
def edit_game(id):
    game = game_repository.select(id)
    developers = developer_repository.select_all()
    return render_template('games/edit.html', game = game, all_developers = developers)

@games_blueprint.route("/games/<id>", methods=['POST'])
def update_game(id):
    title = request.form['title']
    developer_id = request.form['developer_id']
    genre = request.form['genre']
    description = request.form['description']
    stock = request.form['stock']
    buy = request.form['buy']
    sell = request.form['sell']
    
    developer = developer_repository.select(developer_id)

    game = Game(title, genre, description, stock, buy, sell, developer, id)
    game_repository.update(game)
    return redirect("/games")

@games_blueprint.route("/games/genre", methods=['POST'])
def filter_genre():
    genre = request.form['genre']
    all_games = game_repository.filter_genre(genre)
    return render_template("games/index.html", all_games= all_games, genre = genre)

@games_blueprint.route("/games/developer", methods=['POST'])
def filter_developer():
    developer_id = request.form['developer']
    all_games = game_repository.filter_developer(developer_id)
    return render_template("games/index.html", all_games = all_games, developer=developer)