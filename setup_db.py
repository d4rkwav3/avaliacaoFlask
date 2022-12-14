from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker as sm
from datetime import datetime as dt, time as t
import os

def create_database():
    print("Criando nova base de dados na raiz do projeto...")
    caminho = os.path.abspath(os.getcwd())
    engine = create_engine("sqlite:///" + caminho + "/db.sqlite3", echo=True)
    Base = declarative_base()

    class User(Base):
        __tablename__ = "User"
        id = Column(Integer, primary_key=True, autoincrement=True)
        cpf = Column(String(11), nullable=False)
        nome = Column(String(150), nullable=False)
        idade = Column(Integer, nullable=False)
        fone = Column(String(11), nullable=False)
        email = Column(String(150), nullable=False)
        appointments = relationship("Appointment", backref='user')

        def __repr__(self) -> str:
            return f"\nUsuário [{self.id}]: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}\nTelefone: {self.fone}\nE-mail: {self.email}"

        def __init__(self, nome:str, cpf:str, idade:int, fone:str, email:str) -> None:
            self.nome = nome
            self.cpf = cpf
            self.idade = idade
            self.fone = fone
            self.email = email

    class Appointment(Base):
        __tablename__ = "Appointment"
        id = Column(Integer, primary_key=True, autoincrement=True)
        data = Column(Date, nullable=False)
        hora = Column(Time, nullable=False)
        local = Column(String(50), nullable=False)
        doctor = Column(String(150), nullable=False)
        client_id = Column(Integer, ForeignKey('User.id'))

        def __repr__(self) -> str:
            return f"\nConsulta [{self.id}]: Para {self.user_id.nome}\nLocal: {self.local}\nData: {dt.strptime(self.data, '%d-%m-%Y')}\nHora: {self.hora}\n Doutor(a): {self.doctor}"

        def __init__(self, data:dt, hora:t, local:str, doctor:str, user:User) -> None:
            self.data = data
            self.hora = hora
            self.local = local
            self.doctor = doctor
            self.client_id = user

    Base.metadata.create_all(engine)

    print("Base de dados criada com sucesso!")

    q = input("Deseja inserir dados de teste na base? ('S'im/'N'ão)\n")

    if q == 'S' or q == 's' or q == "Sim" or q == "sim":
        test_user = User("Fulano de Tal", "12345678910", 25, "123456789", "teste@teste.com")
        Session = sm(bind=engine)
        session = Session()

        session.add(test_user)
        session.commit()

        test_appointment = Appointment(dt.strptime("20220930", "%Y%m%d"), t(9,0,0), "Internet, sala GitHub", "Flask", 1)
        session.add(test_appointment)
        session.commit()

        print("Dados de teste inseridos com sucesso!")
    else:
        print("Nenhuma modificação feita na base de dados.")
