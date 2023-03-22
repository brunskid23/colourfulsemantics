from flask import Flask, render_template, request, session, redirect, flash
import random
from flask_session import Session
import os

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Setup inital card order
# Dynamically updates based on file names. Allows adding to folder using name.jpg or who-doing-what-where.jpg for scene.
#TODO - add seperators for multi correct answers i.e. grass/park boy/baby

who = os.listdir("static/who")
for item in range(len(who)):
    who[item] = "static/who/" + who[item]

doing = os.listdir("static/doing")
for item in range(len(doing)):
    doing[item] = "static/doing/" + doing[item]

what = os.listdir("static/what")
for item in range(len(what)):
    what[item] = 'static/what/' + what[item]

where = os.listdir("static/where")
for item in range(len(where)):
    where[item] = "static/where/" + where[item]

scene = os.listdir("static/scene")
for item in range(len(scene)):
    scene[item] = "static/scene/" + scene[item]

sel = ["who", "doing", "what", "where"]





@app.route("/", methods=["GET", "POST"])
def index():
    # TODO: add if none of the top row are default then autorun submit
    # Add points system, mario styled
    # Buy a star for x points
    # Add accounts and record correct/incorrects, highscores etc later
    if request.args.get("choice", None) != None:
        choice = request.args.get("choice", None).split("/")
        session["top_row"][choice[1]] = request.args.get("choice", None)

        if choice[1] == "who":
            y = doing
            z = 1
        elif choice[1] == "doing":
            y = what
            z = 2
        elif choice[1] == "what":
            y = where
            z = 3
        else:
            y = where
            z = 3
        return render_template("index.html", top=session["top_row"], select=check_answer(y, z), scene=scene[0])
    if request.args.get("select", None) == "who":
        return render_template("index.html", top=session["top_row"], select=check_answer(who, 0), scene=scene[0])
    elif request.args.get("select", None) == "doing":
        return render_template("index.html", top=session["top_row"], select=check_answer(doing, 1), scene=scene[0])
    elif request.args.get("select", None) == "what":
        return render_template("index.html", top=session["top_row"], select=check_answer(what, 2), scene=scene[0])
    elif request.args.get("select", None) == "where":
        return render_template("index.html", top=session["top_row"], select=check_answer(where, 3), scene=scene[0])
    else:
        session["top_row"] = {}
        session["answers"] = {}
        session["top_row"]["who"] = "static/row/who.jpg"
        session["top_row"]["doing"] = "static/row/doing.jpg"
        session["top_row"]["what"] = "static/row/what.jpg"
        session["top_row"]["where"] = "static/row/where.jpg"
        random.shuffle(who)
        random.shuffle(scene)
        session["answers"] = scene[0].rstrip(".jpg").replace("static/scene/","").split("-")
        return render_template("index.html", top=session["top_row"], select=check_answer(who, 0)[0:6], scene=scene[0])

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/submit")
def submit():
    print(session["answers"])
    print(session["top_row"])
    guess = []
    for verb in sel:
        guess.append(session["top_row"][verb])
    for each in range(len(guess)):
        guess[each] = (guess[each].split(".")[0]).split("/")[2]
        if session["answers"][each] == "any":
            guess[each] = "any"


    print(guess)
    if guess == session["answers"]:
        flash("Well done! You got the sentence correct!", "success")
        print("WINNER WINNER CHICKEN DINNER")
    else:
        flash("Whoops that wasn't quite right!", "danger")
    return redirect("/")

# Shuffle full deck and check answer is included in the first six, if not add then return 6 options
def check_answer(list, x):
    random.shuffle(list)
    first_six = list[0:6]
    if (session['answers'][x]) == "any":
        return first_six
    if ((f"static/{sel[x]}/{session['answers'][x]}.jpg") in first_six) == False:
        print(f"{session['answers'][x]} not {first_six}")
        if session["answers"][x] == "any":
            return list
        first_six[0] = f"static/{sel[x]}/{session['answers'][x]}.jpg"
        random.shuffle(first_six)
        print(first_six)
    return first_six
