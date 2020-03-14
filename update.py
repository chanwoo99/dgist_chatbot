# -*- coding: utf8 -*-
import time

import requests
from bs4 import BeautifulSoup
import json


#json 형식으로 바꾸는 함수
def encode_json(data,bus_type):
    card=[]
    for i in data:
        temp={}
        temp["description"]=i
        card.append(temp)
    datasend={"contents":[{"type": "card.text", "cards": card}], "quickReplies": [
    {
      "type": "text",
      "label": "타는곳 보기",
      "message": bus_type+" 타는곳",
    }
  ]}
    return datasend

def encode_json_location(data):
    card=[]
    for i in data:
        temp={}
        temp["description"]=i
        card.append(temp)
    datasend={"contents":[{"type": "card.text", "cards": card}]}
    return datasend

#json 업데이트 함수
def bus_update():
    req = requests.get('https://www.dgist.ac.kr/kr/html/sub04/0406.html')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    #통근버스 출근버스
    aa=soup.select('#content2 > div:nth-child(2) > table > tbody')[0].find_all('td')
    data_1_go=[]  # 출력값
    for i in range(len(aa)):
        if i%4 == 0:
            continue
        elif i%4 == 1:
            data_1_go.append(aa[i].text)
            continue
        elif i%4 ==2 :
            data_1_go[i//4]=data_1_go[i//4]+" 노선: "+aa[i].text
            continue
        elif i%4 ==3 :
            data_1_go[i//4]=data_1_go[i//4]+" 차량: "+aa[i].text
            continue

    #통근버스 퇴근버스
    aa=soup.select('#content2 > div:nth-child(5) > table > tbody')[0].find_all('td')
    data_1_out=[]  # 출력값
    for i in range(len(aa)):
        if i%4 == 0:
            continue
        elif i%4 == 1:
            data_1_out.append(aa[i].text)
            continue
        elif i%4 ==2 :
            data_1_out[i//4]=data_1_out[i//4]+" 노선: "+aa[i].text
            continue
        elif i%4 ==3 :
            data_1_out[i//4]=data_1_out[i//4]+" 차량: "+aa[i].text
            continue

    #통근버스 출근버스 승차지역
    aa=soup.select('#content2 > ul:nth-child(3) > li > div.ui-text > dl')[0].find_all('dt')
    bb=soup.select('#content2 > ul:nth-child(3) > li > div.ui-text > dl')[0].find_all('dd')
    location_a=[]
    location_b=[]

    for i in range(len(aa)):
        location_a.append(aa[i].text)
        location_b.append(bb[i].text)

    data_1_go_location=[]   #출력값
    for i1, i2 in zip(location_a,location_b):
        data_1_go_location.append(i1+" : "+i2)


    #퇴근버스 출근버스 승차지역
    aa=soup.select('#content2 > ul:nth-child(6) > li > div.ui-text > dl')[0].find_all('dt')
    bb=soup.select('#content2 > ul:nth-child(6) > li > div.ui-text > dl')[0].find_all('dd')
    location_a=[]
    location_b=[]

    for i in range(len(aa)):
        location_a.append(aa[i].text)
        location_b.append(bb[i].text)

    data_1_out_location=[]  # 출력값
    for i1, i2 in zip(location_a,location_b):
        data_1_out_location.append(i1+" : "+i2)













    #셔틀버스
    req = requests.get('https://www.dgist.ac.kr/kr/html/sub04/0406.html?sch_tab=tab3')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    #김천구미역 방면

    aa=soup.select('#content3 > div:nth-child(2) > table > tbody')[0].find_all('td')
    data_2_1=[]  # 출력값
    for i in range(len(aa)):
        if i%4 == 0:
            continue
        elif i%4 == 1:
            data_2_1.append(aa[i].text)
            continue
        elif i%4 ==2 :
            data_2_1[i//4]=data_2_1[i//4]+" 노선: "+aa[i].text
            continue
        elif i%4 ==3 :
            data_2_1[i//4]=data_2_1[i//4]+" 차량: "+aa[i].text
            continue



    #승하차지역
    aa=soup.select('#content3 > ul:nth-child(4) > li > div.ui-text > dl')[0].find_all('dt')
    bb=soup.select('#content3 > ul:nth-child(4) > li > div.ui-text > dl')[0].find_all('dd')
    location_a=[]
    location_b=[]

    for i in range(len(aa)):
        location_a.append(aa[i].text)
        location_b.append(bb[i].text)

    data_2_1_location=[]  # 출력값
    for i1, i2 in zip(location_a,location_b):
        data_2_1_location.append(i1+" : "+i2)





    #대곡 방면

    aa=soup.select('#content3 > div:nth-child(6) > table > tbody')[0].find_all('td')
    data_2_2=[]  # 출력값
    for i in range(len(aa)):
        if i%4 == 0:
            continue
        elif i%4 == 1:
            data_2_2.append(aa[i].text)
            continue
        elif i%4 ==2 :
            data_2_2[i//4]=data_2_2[i//4]+" 노선: "+aa[i].text
            continue
        elif i%4 ==3 :
            data_2_2[i//4]=data_2_2[i//4]+" 차량: "+aa[i].text
            continue



    #승하차지역
    aa=soup.select('#content3 > ul:nth-child(8) > li > div.ui-text > dl')[0].find_all('dt')
    bb=soup.select('#content3 > ul:nth-child(8) > li > div.ui-text > dl')[0].find_all('dd')
    location_a=[]
    location_b=[]

    for i in range(len(aa)):
        location_a.append(aa[i].text)
        location_b.append(bb[i].text)

    data_2_2_location=[]  # 출력값
    for i1, i2 in zip(location_a,location_b):
        data_2_2_location.append(i1+" : "+i2)


    #테크노폴리스 방면

    aa=soup.select('#content3 > div:nth-child(10) > table > tbody')[0].find_all('td')
    data_2_3=[]  # 출력값
    for i in range(len(aa)):
        if i%4 == 0:
            continue
        elif i%4 == 1:
            data_2_3.append(aa[i].text)
            continue
        elif i%4 ==2 :
            data_2_3[i//4]=data_2_3[i//4]+" 노선: "+aa[i].text
            continue
        elif i%4 ==3 :
            data_2_3[i//4]=data_2_3[i//4]+" 차량: "+aa[i].text
            continue



    #승하차지역
    aa=soup.select('#content3 > ul:nth-child(12) > li > div.ui-text > dl')[0].find_all('dt')
    bb=soup.select('#content3 > ul:nth-child(12) > li > div.ui-text > dl')[0].find_all('dd')
    location_a=[]
    location_b=[]

    for i in range(len(aa)):
        location_a.append(aa[i].text)
        location_b.append(bb[i].text)

    data_2_3_location=[]  # 출력값
    for i1, i2 in zip(location_a,location_b):
        data_2_3_location.append(i1+" : "+i2)






    #json 파일로 저장
    #통근버스
    with open('json/data_1_go.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json(data_1_go,"출근버스"), make_file, indent="\t")

    with open('json/data_1_go_location.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json_location(data_1_go_location), make_file, indent="\t")

    #퇴근버스
    with open('json/data_1_out.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json(data_1_out,"퇴근버스"), make_file, indent="\t")

    with open('json/data_1_out_location.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json_location(data_1_out_location), make_file, indent="\t")
    #김천구미
    with open('json/data_2_1.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json(data_2_1,"김천구미"), make_file, indent="\t")

    with open('json/data_2_1_location.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json_location(data_2_1_location), make_file, indent="\t")

    #대곡
    with open('json/data_2_2.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json(data_2_2,"대곡"), make_file, indent="\t")

    with open('json/data_2_2_location.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json_location(data_2_2_location), make_file, indent="\t")
    #테크노폴리스
    with open('json/data_2_3.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json(data_2_3,"테크노폴리스"), make_file, indent="\t")

    with open('json/data_2_3_location.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json_location(data_2_3_location), make_file, indent="\t")

#자동 업데이트 하루에 한번씩
while True:
    bus_update()
    time.sleep(60)
