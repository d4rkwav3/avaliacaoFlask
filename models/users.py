from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..extensions import database as db

class User(db.Model):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    cpf = Column(String(11), nullable=False)
    idade = Column(Integer, nullable=False)
    fone = Column(String(11), nullable=False)
    email = Column(String(150), nullable=False)
    appointments = relationship("Appointment", backref='client')

    def __repr__(self) -> str:
        return f"\nUsuário [{self.id}]: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}\nTelefone: {self.fone}\nE-mail: {self.email}"

    def __init__(self, nome:str, cpf:str, idade:int, fone:str, email:str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.fone = fone
        self.email = email