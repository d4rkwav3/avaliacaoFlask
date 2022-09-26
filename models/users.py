from ..extensions import database as db
from ..models import appointment as ap

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    fone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(150), nullable=False)

    def __repr__(self) -> str:
        return f"\nUsuário [{self.id}]: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}\nTelefone: {self.fone}\nE-mail: {self.email}"

    def __init__(self, nome:str, cpf:str, idade:int, fone:str, email:str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.fone = fone
        self.email = email