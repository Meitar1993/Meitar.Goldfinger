from flask import Flask, render_template, request, session, redirect
from random import getrandbits
import mysql.connector

app = Flask(__name__)
app.secret_key = '123'
from pages.Assignment10.Assignment10 import Assignment10
app.register_blueprint(Assignment10)

@app.route('/')
def Main():
    return render_template("cv.html")


@app.route('/My CV')
def MyCV():
    return render_template("MyCV.html")


@app.route('/Contact Me')
def Contactme():
    return render_template("ContactMe.html")


@app.route('/My Projects')
def projects():
    return render_template("Projects.html")


@app.route('/Recommandations')
def Welcome_Customer():
    return render_template("RecommandationsNew.html")


@app.route('/Assignment8')
def Assignment8():
    isUser = bool(getrandbits(1))
    if isUser:
        name = {'FirstName': "Meitar", 'LastName': "Goldfinger"}
    else:
        name = ''
    return render_template("Assignment8.html", name=name,
                           Hobbies=['Practice Yoga', 'Listen to music', 'Eat', 'Shopping'])


@app.route('/Assignment8Block')
def Assignment8B():
    isUser = bool(getrandbits(1))
    if isUser:
        name = {'FirstName': "Meitar", 'LastName': "Goldfinger"}
    else:
        name = ''
    return render_template("Block.html", name=name, Hobbies=['Practice Yoga', 'Listen to music', 'Eat', 'Shopping'])


@app.route('/Assignment9', methods=["GET", "POST"])
def Assignment9():
    users = {"michaellaw":"Michael Lawson", "lindsayfer":"Lindsay Ferguson",  "tobiasfun":"Tobias Funke",
             "byronfie":"Byron Fields", "georgeedw":"George Edwards", "rachelhow":"Rachel Howell"}
    username = ''
    usernamesrc = ''
    search = False

    if request.method == "GET":
        if 'usernamesrc' in request.args:
            usernamesrc = request.args['usernamesrc']
            search = True
        else:
            usernamesrc = ''

    elif request.method == "POST":
        if 'username' in request.form:
            username = request.form['username']
        else:
            username = ''
        if username in users:
            session['fullname'] = users[username]
        else:
            session['fullname'] = ''
    else:
        username, usernamesrc = '', ''

    return render_template('Assignment9.html',
                           curr_method=request.method,
                           username=username,
                           users=users,
                           usernamesrc=usernamesrc,
                           search=search)

@app.route("/Logout")
def logout():
    session['fullname'] = ''
    return redirect('/Assignment9')



if __name__ == '__main__':
    app.run()