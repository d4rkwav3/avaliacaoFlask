from ..extensions import database as db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    fone = db.Column(db.String(9), nullable=False)
    email = db.Column(db.String(150), nullable=False)

    def __repr__(self) -> str:
        return f"\nUsuário: {self.nome}\nIdade: {self.idade}\nTelefone: {self.fone}\nE-mail: {self.email}"