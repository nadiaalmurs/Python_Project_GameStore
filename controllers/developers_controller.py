from flask import Flask, redirect, render_template, request
from repositories import developer_repository
from repositories import game_repository
from models.game import Game

from flask import Blueprint

developers_blueprint = Blueprint("developers", __name__)

@developers_blueprint.route("/developers")
def developers():
    developers = developer_repository.select_all()
    return render_template("developers/index.html", all_developers = developers)

@developers_blueprint.route("/developers/<id>/delete", methods=['POST'])
def delete_developer(id):
    developer_repository.delete(id)
    return redirect("/developers")

