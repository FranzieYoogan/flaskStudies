

from flask import Flask, json, render_template, request
import flask
import requests


app = Flask(__name__)  # Setup the flask app by creating an instance of Flask


    


@app.route("/", methods = ['POST','GET'])
def index():
 if flask.request.method == 'POST':
    data = request.form['inputValue'];

    api_url = f'https://api.mcsrvstat.us/3/{data}';
    response = requests.get(api_url);
    response.json();

    data = response.text;
    parse_json = json.loads(data);
    dataOnline = parse_json['online'];


    
    print(dataOnline);    
    return render_template("index.htm", dataOnline = str(dataOnline));


 return render_template('index.htm');

if __name__ == '__main__':  
   app.run(debug=True)