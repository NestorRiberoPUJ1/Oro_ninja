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
        session["attemps"] = 0
        session["button"] = ""
        start = False

    return render_template("index.html")


@app.route("/process_money", methods=["POST"])
def process_money():
    global start

    session["attemps"] += 1

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tipo = request.form["type"]
    color = "cl-green"
    gain = "Earned"

    if(session["attemps"] >= 15):
        if(session["golds"] >= 500):
            session["button"] = "<button type=\"submit\">Winner</button>"
        else:
            session["button"] = "<button type=\"submit\">Looser</button>"
    if(tipo == "reset"):
        start = True
        return redirect("/")

    earning = {
        "farm": random.randint(10, 20),
        "cave": random.randint(5, 10),
        "house": random.randint(2, 5),
        "casino": random.randint(-50, 50)
    }

    if (earning[tipo] < 0):
        color = "cl-red"
        gain = "Wasted"

    session["golds"] += earning[tipo]
    session["goldHistoric"].append(
        [color, f"{gain} {earning[tipo]} golds from the {tipo} ({now})"])

    return redirect("/")


if(__name__ == "__main__"):
    app.run(debug=True)
