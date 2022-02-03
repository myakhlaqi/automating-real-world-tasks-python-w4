#!/usr/bin/env python3

import datetime
import os
import reports
import os.path
import run
import emails

from datetime import datetime

def get_product_list(path):
    feedback_list = []
    txtfiles=[
        os.path.join(path, item) for item in os.listdir(path)
        if item.endswith(".txt")
    ]
    for f in txtfiles:
        x = run.extract_feedback_object(f)
        feedback_list.append({"name":x["name"],"weight":str(x["weight"])+" lbs"})
        #print(extract_feedback(f))
    return feedback_list

if __name__ == "__main__":

#    today=datetime.strftime(datetime.today,"%b %d, %Y")
    now = datetime.now() # current date and time
    report_title = 'Processed Update on {0}'.format(now.strftime("%b %d, %Y"))
    reports.generate_report("./tmp/processed.pdf",report_title,get_product_list("./supplier-data/descriptions"))
    message=emails.generate_email("automation@example.com","username@example.com",
                          "Upload Completed - Online Fruit Store",
                          "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                          "./tmp/processed.pdf")
    emails.send_email(message)
    #to check the result open this link on browser:
    #[linux-instance-external-IP]/webmail

