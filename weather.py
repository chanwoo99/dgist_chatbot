# -*- coding: utf8 -*-
from requests import get  # to make GET request

import json
import os
#os.chdir("/home/ubuntu/dgist_chatbot")

def download(url, file_name):
    with open(file_name, "wb") as file:   # open in binary mode
        response = get(url)               # get request
        file.write(response.content)      # write to file




def encode_json(data):
    card=[]
    for i in data:
        temp={}
        temp["description"]=i
        card.append(temp)
    datasend={"contents":[{"type": "card.text", "cards": card}]}
    return datasend


import xml.etree.ElementTree as elemTree

def run_weather():

    url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2771026500"
    download(url,"weather_data.xml")
    
    tree = elemTree.parse('weather_data.xml')
    root = tree.getroot()

    data=root[0][6][5][1]
    date=root[0][5]

    pre_data=[]

    for i in data:
        text=date.text+"업데이트 \n" + "시간 : "+i[0].text + "\n" + "온도 : " + i[2].text +"\n" + "날씨 : " + i[7].text + "\n" + "강수확률 : " + i[9].text + "%"
        pre_data.append(text)


    with open('json/weather.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json(pre_data), make_file, indent="\t")
