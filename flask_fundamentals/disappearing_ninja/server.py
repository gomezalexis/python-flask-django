from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/ninja/')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>/')
def ninja_color(color):
    turtle = ''
    colors = ['orange', 'blue', 'red', 'purple']

    if color in colors:
        turtle = color
    else:
        turtle = 'april'
    print "The selected color is {}".format(turtle)
    return render_template("color.html", turtle=turtle)

app.run(debug=True)