from flask import Blueprint, render_template
from ..extensions import database as db
from ..models.users import User

list_clients = Blueprint("list", __name__)

@list_clients.route("/list")
def client_list():
    db_query = User.query.all()
    return render_template("list.html", clientes=db_query), 200