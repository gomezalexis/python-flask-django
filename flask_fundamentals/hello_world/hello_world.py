from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
                                          # following function to the '/' route. This means that
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # the following "hello_world" function.
def hello():
  return render_template('hello.html') 

app.run(debug=True)