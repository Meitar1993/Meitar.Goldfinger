from flask import Flask, redirect, url_for
from random import getrandbits

app = Flask(__name__)

@app.route('/')
def Welcome_Main():
    return 'Welcome To the Main Page!'

@app.route('/about')
def Welcome_About():
    return 'Welcome To About Page!'

@app.route('/home')
def Welcome_Home():
    return redirect('/')

@app.route('/customers')
def Welcome_Customer():
    IsSign = bool(getrandbits(1))
    print(IsSign)
    if IsSign:
        return redirect(url_for('Welcome_Home'))
    else:
        return 'You need to signup'

if __name__ == '__main__':
    app.run()
