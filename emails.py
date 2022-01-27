#!/usr/bin/env python3

from email.message import EmailMessage
import getpass
import mimetypes
import os
from re import sub
import smtplib
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate

def generate_email(sender,recipient, subject,email_body,attachment_file):
    message = EmailMessage()
    # sender = "yahya.akhlaghi@gmail.com"
    # recipient = "csmaster90@hotmail.com"
    message["From"] = sender
    message["To"] = recipient

    #message["Subject"] = "Greetings from {} to {}!".format(sender, recipient)
    message["Subject"] = subject

    # body = """Hey there!

    # I'm learning to send emails using Python!"""
    message.set_content(email_body)

    #attachment_file = "./tmp/processed.pdf"
    attachment_filename = os.path.basename(attachment_file)

    mime_type, _ = mimetypes.guess_type(attachment_file)
    print(mime_type)

    mime_type, mime_subtype = mime_type.split("/", 1)

    with open(attachment_file, "rb") as ap:
        message.add_attachment(
            ap.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=os.path.basename(attachment_file),
        )

        
    return message
def send_email(message):

    mail_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    mail_server.set_debuglevel(1)

    mail_pass = getpass.getpass("Password? ")
    mail_server.login(message["From"], mail_pass)
    mail_server.send_message(message)
    mail_server.quit()
    
