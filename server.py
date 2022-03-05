from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "MiLlavesita"
start = True


@app.route("/")
def formulario():
    global start

    if(start):
        session.clear()
        session["goldHistoric"] = []
        session["golds"] = 0
        start = False

    return render_template("index.html")


@app.route("/process_money", methods=["POST"])
def process_money():
    global start

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tipo = request.form["type"]
    color = "cl-green"
    gain = "Earned"
    if(tipo == "reset"):
        start= True
        return redirect("/")

    elif(tipo == "farm"):
        earning = random.randint(10, 20)
    elif(tipo == "cave"):
        earning = random.randint(5, 10)
    elif(tipo == "house"):
        earning = random.randint(2, 5)
    elif(tipo == "casino"):
        earning = random.randint(-50, 50)
        if (earning < 0):
            color = "cl-red"
            gain = "Wasted"
    session["golds"] += earning
    session["goldHistoric"].append(
        [color, f"{gain} {earning} golds from the {tipo} ({now})"])

    return redirect("/")


if(__name__ == "__main__"):
    app.run(debug=True)
