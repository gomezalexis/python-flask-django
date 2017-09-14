from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAMES_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe' #session needs secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    pass_confirmation = request.form['pass_confirmation']
    # validation here
    if len(first_name) < 1 or len(last_name) < 1 or len(email) < 1 or len(password) < 1 or len(pass_confirmation) < 1:
        flash("You cannot leave any field empty")
    
    elif not EMAIL_REGEX.match(email):
        flash("Invalid email format")
    
    elif not NAMES_REGEX.match(first_name) or not NAMES_REGEX.match(last_name):
        flash("Name and Last name should only contain letters")
    
    elif pass_confirmation != password:
        flash("Password doesn't match!")
    else:
        flash("Great! Everything was validated")

    
    return redirect('/')


app.run(debug=True)