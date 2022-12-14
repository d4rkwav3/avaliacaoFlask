from flask import Blueprint, render_template, redirect, url_for, request
from ..extensions import database as db
from ..models.users import User
from ..models.appointment import Appointment
from ..models.places import places
from ..models.doctors import doctors
from ..models.meses import meses
from datetime import datetime as dt, time as t

aptm = Blueprint("Appointment", __name__)

@aptm.route("/add_ap")
def new_appointment():
    users = User.query.all()
    return render_template("add_ap.html", users=users, doctors=doctors, places=places), 200

@aptm.route("/ap/add", methods=['POST'])
def add_appointment():
    user_id = int(request.form["id"])
    local = request.form["local"]
    doctor = request.form["doutores"]
    data = dt.strptime(request.form["data"], "%Y-%m-%d")
    hora = t(int(request.form["hora"][0:2]), int(request.form["hora"][3:5]))

    appointment = Appointment(data, hora, local, doctor, user_id)

    db.session.add(appointment)
    db.session.commit()
    return redirect(url_for("home.home_page"))

@aptm.route("/check_date", methods=['GET'])
def check_date():
    return render_template("ap_list.html"), 200

@aptm.route("/date", methods=['POST'])
def view_appointments():
    data = dt.strptime(request.form["data"], "%Y-%m-%d")
    datastr = str(data)
    ano = int(datastr[0:4])
    mes_number = int(datastr[5:7])
    mes_letters = meses.get(int(datastr[5:7]))
    dia = int(datastr[8:10])

    date_query = Appointment.query.filter_by(data=data.strftime("%Y-%m-%d"))
    return render_template("date_list.html", dia=dia, mes_number=mes_number, mes_letters=mes_letters, ano=ano, data=date_query), 200