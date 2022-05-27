from db.run_sql import run_sql

from models.developer import Developer
from models.game import Game
from repositories import developer_repository

def save(game):
    sql = "INSERT INTO games (title, genre, description, stock_quantity, buying_price, selling_price, developer_id) VALUES (?, ?, ?, ?, ?, ?, ?) RETURNING *"
    values = [game.title, game.genre, game.description, game.stock_quantity, game.buying_price, game.selling_price, game.developer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    return game

def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)

    for row in results:
        developer = developer_repository.select(row['developer_id'])
        game = Game(row['title'], row['genre'], row['description'], row['stock_quantity'], row['buying_price'], row['selling_price'], developer, row['id'])
        games.append(game)

    return games

def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id =?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        developer = developer_repository.select(row['developer_id'])
        game = Game(result['title'], result['genre'], result['description'], result['stock_quantity'], result['buying_price'], result['selling_price'], developer, result['id'])
    return game

def delete_all():
    sql="DELETE FROM games"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM games WHERE id = ?"
    values=[id]
    run_sql(sql, values)

def update(game):
    sql = "UPDATE games SET (title, genre, description, stock_quantity, buying_price, selling_price, developer_id) = (?, ?, ?, ?, ?, ?, ?) WHERE id = ?"
    values = [game.title, game.genre, game.description, game.stock_quantity, game.buying_price, game.selling_price, game.developer.id]
    run_sql(sql, values)