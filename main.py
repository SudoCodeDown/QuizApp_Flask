from flask import Flask, render_template, url_for, request, redirect
from create_quiz import quiz as q

app = Flask(__name__)


@app.route('/')
def view():
    return render_template("base.html")

@app.route('/admin/', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Copy_Cat_2050' or request.form['password'] != 'DataSecurity@12345':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('create_quiz'))
    return render_template("admin_login.html", error=error)

@app.route('/admin/create_quiz')
def create_quiz():
    return render_template("create_quiz.html")

@app.route('/<quiz>/')
def quiz(quiz):
    return render_template("quiz.html", questions=q[quiz])


if(__name__ == "__main__"):
    app.run(debug=True)
