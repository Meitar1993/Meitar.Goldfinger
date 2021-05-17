from flask import Flask, render_template
from random import getrandbits

app = Flask(__name__)

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
    isUser =bool(getrandbits(1))
    if isUser:
        name = {'FirstName': "Meitar", 'LastName': "Goldfinger"}
    else:
        name = ''
    return render_template("Assignment8.html", name=name, Hobbies=['Practice Yoga', 'Listen to music', 'Eat', 'Shopping'])


@app.route('/Assignment8Block')
def Assignment8B():
    isUser =bool(getrandbits(1))
    if isUser:
        name = {'FirstName': "Meitar", 'LastName': "Goldfinger"}
    else:
        name = ''
    return render_template("Block.html", name=name, Hobbies=['Practice Yoga', 'Listen to music', 'Eat', 'Shopping'])


if __name__ == '__main__':
    app.run()

