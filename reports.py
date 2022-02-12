#!/usr/bin/env python3

from datetime import date, datetime
import smtplib
import os.path
import mimetypes
import getpass

from email.message import EmailMessage
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate

def generate_report(attachment, title, paragraph):
 
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()

    report_title= Paragraph(title, styles["h1"])
    
    product_list=""
    for item in paragraph:
        product_list+="name: {0}<br/>weight: {1}<br/><br/>".format(item["name"],item["weight"])
    body= Paragraph(product_list,styles["Normal"])
    #print(table_data)

    report.build([report_title, body])


#generate_report("./tmp/processed.pdf",report_title,)
