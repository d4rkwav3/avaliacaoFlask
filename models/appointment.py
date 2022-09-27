from ..extensions import database as db
#from ..models.users import User
from datetime import datetime, time

class Appointment(db.Model):
    __tablename__ = "appointment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    local = db.Column(db.String(50), nullable=False)
    doctor = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f"\nConsulta [{self.id}]: Para {self.user_id.nome}\nLocal: {self.local}\nData: {datetime.strptime(self.data, '%d-%m-%Y')}\nHora: {self.hora}\n Doutor(a): {self.doctor}"

    def __init__(self, data:datetime, hora:time, local:str, doctor:str, user:int) -> None:
        self.data = data
        self.hora = hora
        self.local = local
        self.doctor = doctor
        self.user_id = user