from flask import Blueprint, render_template, redirect, url_for, request
from ..extensions import database as db
from ..models.users import User

list_clients = Blueprint("list", __name__)

@list_clients.route("/list")
def client_list():
    db_query = User.query.all()
    return render_template("list.html", clientes=db_query), 200

@list_clients.route("/list/update/<client_id>")
def update_form(client_id=0):
    client = User.query.filter_by(id=client_id).first()
    return render_template("update_c.html", client=client), 200

@list_clients.route("/list/upd", methods=['POST'])
def update_client():
    id = request.form["id"]
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    idade = request.form["idade"]
    fone = request.form["telefone"]
    email = request.form["email"]

    user = User.query.filter_by(id = id).first()
    user.nome = nome
    user.cpf = cpf
    user.idade = idade
    user.fone = fone
    user.email = email

    db.session.add(user)
    db.session.commit()
    return redirect(url_for("list.client_list"))
