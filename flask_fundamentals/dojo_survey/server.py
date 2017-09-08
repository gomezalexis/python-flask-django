from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def ask_questions():
    print request.form
    name = request.form['firstname']
    language = request.form['language']
    location = request.form['location']
    comment = request.form['comment']
    print "The name is: {}. The location is {} and the fav language is {}".format(name,location,language)
    print "The comment is: {}".format(comment)
    
    return render_template('result.html', name=name,location=location,language=language,comment=comment)

app.run(debug=True)