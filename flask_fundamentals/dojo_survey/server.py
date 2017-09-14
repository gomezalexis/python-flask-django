from flask import Flask, render_template, redirect, request, flash  

app = Flask(__name__)
app.secret_key = "ThisIsSecret"
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

    if  len(name) < 1:
        flash("The name cannot be empty")
        return redirect('/')
    
    if len(comment) > 120 or len(comment) < 1:
        flash('You need to write more that 1 char and less than 120 in comment area. You wrote {}'.format(len(comment)))
        return redirect('/')

    return render_template('result.html', name=name,location=location,language=language,comment=comment)

app.run(debug=True)