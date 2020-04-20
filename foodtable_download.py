
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

def run_foodtable(no):
    url='https://ecm.dgist.ac.kr/ecm/ecmCommon/file/downloadFile.do?ATFILE_CONN_NO='+str(no)+'&ATFILE_SEQ_NO='
    for i in range(3):
        download(url+str(i),"foodtable/"+str(i+1)+".xlsx")


from urllib import request
savename = "test2.xlsx"
url = "https://ecm.dgist.ac.kr/ecm/ecmCommon/file/downloadFile.do?ATFILE_CONN_NO=1586737312459&ATFILE_SEQ_NO=0"
mem = request.urlopen(url).read()
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다.")
