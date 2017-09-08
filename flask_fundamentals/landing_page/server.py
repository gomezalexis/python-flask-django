from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def beginning():
    return render_template('index.html')


@app.route('/ninjas')
def ninjas_info():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def first_form():
    return render_template('dojos.html')

app.run(debug=True)