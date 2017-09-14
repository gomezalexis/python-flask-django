from flask import Flask, render_template, request, redirect, session
import random 

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['the_number'] = random.randrange(1,51)

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_the_number():

    isCorrect = False

    print "The number is {}".format(session['the_number'])
    guess = request.form['guess']
    print guess
    if guess < session['the_number']:
        session['too_low'] = "{} is to low".format(guess)
    elif guess > session['the_number']:
        session['too_high'] = "{} is too high".format(guess)
    elif guess == session['the_number']:
        session['won'] = "{} was the number. You won".format(guess)
        isCorrect = True

    return redirect('/')

app.run(debug=True)