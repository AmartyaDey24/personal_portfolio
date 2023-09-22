from flask import Flask, render_template, request
from dates_data import Dates_data
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from flask_mail import Mail, Message

app = Flask(__name__)

#connecting to Xaamp Mysql through sqlalchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/portfolio_amartya"
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'amartyaportfolio@gmail.com'  # Replace with your Gmail email address
app.config['MAIL_PASSWORD'] = 'lsqw vmcy frho ebch'  # Replace with your Gmail password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


def send_email(subject, message, sender_email):
    msg = Message(subject=subject, sender=sender_email, recipients=['amartyadey929@gmail.com@gmail.com'])  # Replace with the recipient's email address
    msg.body = message
    mail.send(msg)

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

        entry = Contacts(name_post, email_post, subject_post, message_post, Dates_data.submit_date)
        db.session.add(entry)
        db.session.commit()
    
        send_email(subject_post, message_post, email_post)

    return render_template('contact.html')

app.run(debug=True)