from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
#from sqlalchemy.orm import relationship
from ..extensions import database as db
#from .users import User
from datetime import datetime, time

class Appointment(db.Model):
        __tablename__ = "Appointment"
        id = Column(Integer, primary_key=True, autoincrement=True)
        data = Column(Date, nullable=False)
        hora = Column(Time, nullable=False)
        local = Column(String(50), nullable=False)
        doctor = Column(String(150), nullable=False)
        client_id = Column(Integer, ForeignKey('User.id'))

        def __repr__(self) -> str:
            return f"\nConsulta [{self.id}]: Para {self.user_id.nome}\nLocal: {self.local}\nData: {datetime.strptime(self.data, '%d-%m-%Y')}\nHora: {self.hora}\n Doutor(a): {self.doctor}"

        def __init__(self, data:datetime, hora:time, local:str, doctor:str, user: int) -> None:
            self.data = data
            self.hora = hora
            self.local = local
            self.doctor = doctor
            self.client_id = user