from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
@app.route('/home')
def index():
    return render_template("landing.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup')
def signUp():
    return render_template("signup.html")

@app.route('/signup_submit')
def signupSubmit():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    return render_template("signup_submit.html",fname=fname,lname=lname)