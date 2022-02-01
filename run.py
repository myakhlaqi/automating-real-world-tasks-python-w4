#! /usr/bin/env python3

import json
import os
import requests

def extract_feedback_object(logfile):
    product = {}
    file = open(logfile, "r")

    name, weight,description  = [line.strip() for line in file.readlines()]
    #print(title,name,date,feedback)
    product["name"] = name
    product["weight"] = int(weight.strip(" lbs"))
    product["description"] = description
    product["image_name"] = os.path.basename(logfile).strip(".txt")+".jpeg"
    return product


def upload_product_description(path,url):
    feedback_dic = []
    txtfiles=[
        os.path.join(path, item) for item in os.listdir(path)
        if item.endswith(".txt")
    ]
    for f in txtfiles:
        x = extract_feedback_object(f)
        feedback_dic.append(x)
        #print(extract_feedback(f))
        post_to_webservice(url,x)
    return feedback_dic

def post_to_webservice(url, feedbacks):
    #headers =  {"Content-Type":"application/json"}
    response = requests.post(url, json=feedbacks)
    if (response.status_code == 201):
        print("Submitted!")
    print("inside post:", response.status_code)

#path = ""
#print(extract_feedback("./020.txt"))
#upload_product_description("./supplier-data/descriptions/","http://104.198.221.153/feedback/")
#print(os.path.basename("E:\\programming project\\Python\\Coursera projects\\automating-real-world-tasks-python-w4\\supplier-data\descriptions\\001.txt").strip("txt")+"jpeg")
