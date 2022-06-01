from db.run_sql import run_sql

from models.developer import Developer
from models.game import Game

def save(developer):
    sql = "INSERT INTO developers (name, shipping_price, shipping_time, active) VALUES (?, ?, ?, ?) RETURNING *"
    values = [developer.name, developer.shipping_price, developer.shipping_time, developer.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    developer.id = id
    return developer

def select_all():
    developers = []

    sql = "SELECT * FROM developers"
    results = run_sql(sql)

    for row in results:
        active = True if row['active'] == 1 else False
        developer = Developer(row['name'], row['shipping_price'], row['shipping_time'], active, row['id'])
        developers.append(developer)

    return developers

def select(id):
    developer = None
    sql = "SELECT * FROM developers WHERE id =?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        active = True if result['active'] == 1 else False
        developer = Developer(result['name'], result['shipping_price'], result['shipping_time'], active, result['id'])
    return developer

def delete_all():
    sql="DELETE FROM developers"
    run_sql(sql)

def update(developer):
    sql = "UPDATE developers SET (name, shipping_price, shipping_time, active) = (?, ?, ?, ?) WHERE id = ?"
    values = [developer.name, developer.shipping_price, developer.shipping_time, developer.active, developer.id]
    run_sql(sql, values)