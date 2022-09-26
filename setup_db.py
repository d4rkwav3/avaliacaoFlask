from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker as sm
from datetime import datetime

def create_database():
    engine = create_engine("sqlite:///avaliaçãoFlask/db.sqlite3", echo=True)
    Base = declarative_base()

    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True, autoincrement=True)
        cpf = Column(String(11), nullable=False)
        nome = Column(String(150), nullable=False)
        idade = Column(Integer, nullable=False)
        fone = Column(String(11), nullable=False)
        email = Column(String(150), nullable=False)

        def __repr__(self) -> str:
            return f"\nUsuário [{self.id}]: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}\nTelefone: {self.fone}\nE-mail: {self.email}"

        def __init__(self, nome:str, cpf:str, idade:int, fone:str, email:str) -> None:
            self.nome = nome
            self.cpf = cpf
            self.idade = idade
            self.fone = fone
            self.email = email

    class Appointment(Base):
        __tablename__ = "appointment"
        id = Column(Integer, primary_key=True, autoincrement=True)
        data = Column(Date, nullable=False)
        hora = Column(Time, nullable=False)
        local = Column(String(50), nullable=False)
        doctor = Column(String(150), nullable=False)
        user_id = Column(Integer, ForeignKey('users.id'))
        user = relationship("User", backref = "User")

        def __repr__(self) -> str:
            return f"\nConsulta [{self.id}]: Para {self.user_id.nome}\nLocal: {self.local}\nData: {datetime.strptime(self.data, '%d-%m-%Y')}\nHora: {self.hora}\n Doutor(a): {self.doctor}"

        def __init__(self, data:str, hora:str, local:str, doctor:str, user:int) -> None:
            self.data = data
            self.hora = hora
            self.local = local
            self.doctor = doctor
            self.user_id = user

    #User.appointment = relationship("Appointment", order_by=Appointment.id, back_populates="users")
    Base.metadata.create_all(engine)
    '''
    test_user = User("Teste", "teste", 32, "123456789", "teste@teste.com")
    Session = sm(bind=engine)
    session = Session()

    session.add(bruno)
    session.commit()
    '''