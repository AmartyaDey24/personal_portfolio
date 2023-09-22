from flask import Flask, render_template, request
from dates_data import Dates_data
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#connecting to Xaamp Mysql through sqlalchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/portfolio_amartya"
db = SQLAlchemy(app)

#class contacts help to update the contacts_form table with relevalent data
class Contacts(db.Model):
    '''
    sno, name, email, subject, message, datetime
    '''
    __tablename__ = 'contacts_form' 

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    datetime = db.Column(db.String(10), nullable=True)

    def __init__(self, name, email, subject, message, datetime):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
        self.datetime = datetime


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

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        #Add data to db
        name_post = request.form.get('name')
        email_post = request.form.get('email')
        subject_post = request.form.get('subject')
        message_post = request.form.get('message')

        entry = Contacts(name = name_post, email = email_post, subject = subject_post, message = message_post, datetime = Dates_data.get_submit_datetime)
        db.session.add(entry)
        db.session.commit()
    

    return render_template('contact.html')

app.run(debug=True)