from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def ask_name():   
    print request.form
    name = request.form['name']
    print "Your name: {}".format(name)

    return redirect('/')

app.run(debug=True)

