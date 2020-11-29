from flask import Flask, render_template
from create_quiz import quiz as q

app = Flask(__name__)


@app.route('/')
def view():
    return render_template("base.html")

@app.route('/admin/')
def admin_login():
    return render_template("admin_login.html")

@app.route('/<quiz>/')
def quiz(quiz):
    return render_template("quiz.html", questions=q[quiz])


if(__name__ == "__main__"):
    app.run(debug=True)
