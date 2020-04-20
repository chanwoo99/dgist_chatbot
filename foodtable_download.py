
# -*- coding: utf-8 -*-

from requests import get  # to make GET request

import json
import os
#os.chdir("/home/ubuntu/dgist_chatbot")
os.chdir("C:/Users/chanwoo/Desktop/python_web/dgist_chatbot/dgist_chatbot")

def download(url, file_name):
    with open(file_name, "wb") as file:   # open in binary mode
        response = get(url)               # get request
        file.write(response.content)

download('https://github.com/chanwoo99/dgist_chatbot/blob/master/foodtable/1.xlsx?raw=true','ssss.xlsx')
