from flask import Blueprint, render_template, redirect, url_for, request as r
from ..extensions import database as db
from ..models.users import User;

new = Blueprint("novo", __name__)

@new.route("/novo")
def novo_cadastro():
    return render_template("novo.html"), 200

@new.route("/novo/add", methods=["POST"])
def adicionar():
    nome = r.form["nome"]
    cpf = r.form["cpf"]
    idade = r.form["idade"]
    telefone = r.form["telefone"]
    email = r.form["email"]

    user = User(nome, cpf, idade, telefone, email)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("home.home_page"))