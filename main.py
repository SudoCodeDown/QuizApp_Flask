from flask import Flask, render_template, url_for, request, redirect
from create_quiz import quiz as q

app = Flask(__name__)



#front page
@app.route('/')
def view():
    return render_template("base.html")

#Quiz platfrom
@app.route('/<quiz>/', methods=['GET', 'POST'])
def quiz(quiz):
    score = 0
    total = 0
    if request.method ==  'POST' :
        for answer in request.form:
            if(request.form[answer] == "True"):
                score += 1
            total += 1
        print(score)
        return redirect(url_for('score_generator', quiz=quiz, score=score, total=total))
    return render_template("quiz.html", questions=q[quiz])

@app.route("/<quiz>/score")
def score_generator(quiz):
    score = request.args.get('score', None)
    total = request.args.get('total', None)
    return render_template('score.html', quiz=quiz, score=score, total=total)

#admin
@app.route('/admin/', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Copy_Cat_2050' or request.form['password'] != 'DataSecurity@12345':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('create_quiz'))
    return render_template("admin_login.html", error=error)

@app.route('/admin/create_quiz', methods=['GET','POST'])
def create_quiz():
    error = None
    if request.method == 'POST':
        print(request.form)
    return render_template("create_quiz.html")



if(__name__ == "__main__"):
    app.run(debug=True)
