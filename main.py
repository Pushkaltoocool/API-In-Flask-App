from flask import Flask
from flask import render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/guess/<name>')
def home(name):
    response = requests.get(url=f"https://api.agify.io/?name={name}")
    age = response.json()["age"]
    response = requests.get(f"https://api.genderize.io/?name={name}")
    gender = response.json()["gender"]
    return render_template("index.html", age=age, gender=gender, name=name)



if __name__ == "__main__":
    app.run(debug=True)