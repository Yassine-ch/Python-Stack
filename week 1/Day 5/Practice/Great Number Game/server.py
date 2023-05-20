import random
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "password"


@app.route("/")
def index():

    if "answer" not in session:
        session["answer"] = random.randint(1,100)

    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def process_guess():
    guess = int(request.form["number"])
    if guess > session["answer"]:
        print("Guess is too high")
        session["response"] = "<p>Too high!</p>"


    elif guess < session["answer"]:
        print("Guess is too low")
        session["response"] = "<p>Too low!</p>"
    else:
        print("Guessed the number!")
        session["response"] =f"<p>{guess} was the number!</p><form action='/start_game' method='post'><input type='submit' value='Play again!'></form>"

    return redirect("/")


# stacked routes to restart the game
@app.route("/reset")
@app.route("/start_game", methods=["POST"])
def restart():
    session.clear()
    session["answer"] = random.randint(1,100)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)