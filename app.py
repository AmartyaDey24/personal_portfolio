from flask import Flask, render_template, request,redirect, url_for
from dates_data import Dates_data
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_migrate import Migrate
from exp_data import Exp_data
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)

#connecting to Xaamp Mysql through sqlalchemy
app.config["SQLALCHEMY_DATABASE_URI"] = params["prod_mysql_uri"]
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = params["mail_server"]
app.config['MAIL_PORT'] = params["mail_port"]
app.config['MAIL_USERNAME'] = params["mail_username"]
app.config['MAIL_PASSWORD'] = params["mail_pass"]
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

migrate = Migrate(app, db)

def send_email(subject, message, sender_email, name):
    msg = Message(subject= name + ' from portfolio - ' + subject, sender=sender_email, recipients=[params["recipients_email"]])
    message_format = f"{message}\n\nSender's Email: {sender_email}"
    msg.body = message_format
    mail.send(msg)

#class contacts help to update the contacts_form table with relevalent data
class Contacts(db.Model):

    __tablename__ = params["contact_db_table"] 

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

# Create the table if it doesn't exist (or add columns)
with app.app_context():
    db.create_all()

@app.route("/")
def root():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template('home.html', params = params)

@app.route("/about")
def about():
    exp_months = Dates_data.get_exp_months()
    age = Dates_data.get_age()
    return render_template('about.html', exp_months = exp_months, age = age, params = params)

@app.route("/resume")
def resume():
    return render_template('resume.html', params = params)

@app.route("/experiences")
def experiences():
    exp_months = Dates_data.get_exp_months()
    return render_template('experiences.html', params = params, exp_months = exp_months, exp_data = Exp_data.get_exp_data())

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
    
        send_email(subject_post, message_post, email_post, name_post)

    return render_template('contact.html', params = params)

if __name__ == "__main__":
    
    app.run(debug=True, host="0.0.0.0", port=5000)