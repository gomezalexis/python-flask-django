from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if not session.get('count'):
        session['count'] = 0
        session['to_html'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    da_number = 0
    buildings = {"farm": random.randint(10,20),"cave": random.randint(5,10),
    "house": random.randint(2,5),"casino": random.randint(-50,50)}

    clicked = request.form['building']
    print "The user clicked -{}-.".format(clicked)

    if buildings[clicked]:
        if clicked == 'casino' and session['count']<=0:
            session.modified=True 
            new_comment = "You cannot enter the casino with 0 money $$$"
            session['to_html'].append(new_comment) 
            session['at_start'] = 'You need money to start!!'
            return redirect('/')

        da_number = buildings.get(clicked)
        session['count'] += da_number
        print "The added/substracted number is {}".format(da_number)

    if da_number == 0:
        new_comment = "You stayed even! You earned nothing"
    elif da_number > 0:
        new_comment = "You earned {} gold from the {}!".format(da_number,clicked)
    elif da_number < 0:
        new_comment = "You entered a {} and lost {} gold(s) in the process.. Ouch!".format(clicked,da_number)

    session['to_html'].append(new_comment)    

    print session['count']
    print session['to_html']
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True) # run our server