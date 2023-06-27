import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from .models import Employees
from config.base import settings
from core.utils import  time

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
sendgrid_key = settings.SENDGRID_API_KEY


def get_user_by_email(db: Session, email: str):
    return db.query(Employees).filter(Employees.email==email).first()

def verify_email_password(db:Session , email:str ,password:str):
    userinfo = db.query(Employees).filter(Employees.email==email).first()
    if userinfo:
        if userinfo.password == password :
            return userinfo
    else:
        return None

def get_password(db:Session, email : str):
    userinfo = get_user_by_email(db, email)
    retrieve_password =userinfo.__dict__["password"]
    return retrieve_password

def send_email(sender_email, sender_password, receiver_email, subject, message):
    
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message["Subject"] = subject

    
    email_message.attach(MIMEText(message, "plain"))

    try:
        
        smtp_server = "smtp.gmail.com"  
        port = 587  
        context = smtplib.SMTP(smtp_server, port)

        
        context.starttls()

       
        context.login(sender_email, sender_password)

        
        context.sendmail(sender_email, receiver_email, email_message.as_string())

        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("An error occurred while sending the email:", str(e))
    finally:
        # Quit the SMTP server
        context.quit()
    return True 





    