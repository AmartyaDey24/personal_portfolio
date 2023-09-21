from flask import Flask, render_template
from dates_data import Dates_data


app = Flask(__name__)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    exp_months = Dates_data.get_exp_months()
    age = Dates_data.get_age()
    return render_template('about.html', exp_months = exp_months, age = age)

@app.route("/resume")
def resume():
    return render_template('resume.html')

@app.route("/experiences")
def experiences():
    return render_template('experiences.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

app.run(debug=True)