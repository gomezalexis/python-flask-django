from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    
    session['count'] += 1

    
    return render_template("index.html")

@app.route('/number/')
def add_two():
    session['count'] += 1
    print session['count']
    return redirect('/')

@app.route('/reset/')
def reset():
    session['count'] = 0

    return redirect('/')



# @app.route('/whatever', methods=['POST'])
# def this_random():
#     print "Is working"
#     return redirect('/random/')

# @app.route('/random/')
# def the_random():
#     return render_template('random.html')
app.run(debug=True) # run our server