# -*- coding: utf8 -*-

import pandas as pd
import xlrd
import datetime
import timemodule
import json

week_today=timemodule.today_weekday(datetime.datetime.now())  #오늘이 무슨 요일인지 알려주는 변수
df = pd.read_excel('foodtable/1.xlsx',header=5, names = ['None', "type",'월','화','수','목','금'])
df= df.fillna('없음')

df2 = pd.read_excel('foodtable/2.xlsx',header=1, names = ['None', "type",'월','화','수','목','금'])
df2= df2.fillna('없음')

df3 = pd.read_excel('foodtable/3.xlsx',header=5, names = ['None', "type",'월','화','수','목','금'])
df3= df3.fillna('없음')



#json 형식으로 바꾸는 함수
def encode_json(data):
    card=[]
    for i in data:
        temp={}
        temp["description"]=i
        card.append(temp)
    datasend={"contents":[{"type": "card.text", "cards": card}], "quickReplies": [
    {
      "type": "text",
      "label": "뒤로가기",
      "message": "학식 메뉴 안내",
    }
  ]}
    return datasend
#하나의 문장으로 이어줌
def make_block(data,init,ran):
    text=""
    for i in range(ran):
        if data[i+init]!="없음":

            text+=data[i+init]
            text+="\n"
    return text

def food_update(test_time):
    #일품 정식
    data_1=[]
    data_1.append(test_time)
    data_1.append("A : "+df[week_today][0])
    data_1.append("B : "+df[week_today][1])
    data_1.append("C : "+df[week_today][2])
    data_1.append("셀프코너 : "+df[week_today][3])

    #그냥 정식
    data_2="일반 정식: \n "+make_block(df[week_today],4,6)

    #석식 1
    data_3="석식 1: \n "+make_block(df[week_today],10,6)

    #석식 2
    data_4="석식 2: \n "+make_block(df[week_today],16,6)

    #학생식당 종합
    data_1.append(data_2)
    data_1.append(data_3)
    data_1.append(data_4)

    with open('json/bob/data_1.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json(data_1), make_file, indent="\t")

    #연구동 ab코너
    data_5="중식 A&B: \n "+make_block(df2[week_today],0,13)
    data_6="석식 B: \n "+make_block(df2[week_today],13,6)
    data_7=[data_5,data_6]

    with open('json/bob/data_2.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json(data_7), make_file, indent="\t")

    #교직원
    data_8="중식 : \n "+make_block(df3[week_today],0,9)
    data_9=[data_8]

    with open('json/bob/data_3.json', 'w', encoding='utf-8') as make_file:
        json.dump(encode_json(data_9), make_file, indent="\t")
