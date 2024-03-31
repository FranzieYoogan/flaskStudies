

from flask import Flask, render_template, request
import flask


app = Flask(__name__)  # Setup the flask app by creating an instance of Flask


    


@app.route("/", methods = ['POST','GET'])
def index():
 if flask.request.method == 'POST':
    data = request.form['inputValue'];
    return render_template("index.htm", data = data)


 return render_template('index.htm');

if __name__ == '__main__':  
   app.run(debug=True)