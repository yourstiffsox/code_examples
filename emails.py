import email
import os
import mimetypes
import smtplib

def generate_email(sender, receiver, subject, body, attatchment):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)
   
    attatchment_filename = os.path.basename(attatchment)
    mime_type, _ = mimetypes.guess_type(attatchment)
    mime_type, mime_subtype = mime_type.split('/', 1)
   
    with open(attatchment, 'rb') as ap:
        message.add_attachment(ap.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=os.path.basename(attatchment))
    return message
def generate_health_email(sender, receiver, subject, body):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
