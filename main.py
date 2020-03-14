# -*- coding: utf-8 -*-

import os
from flask import Flask, request, jsonify
import timemodule
import data
import datetime
import json

app = Flask(__name__)

@app.route('/test',methods=['POST'])
def send_date():
    dataReceive = request.get_json()
    event=dataReceive["action"]["params"]["event"]
    if event in data.exam_date:
        event_date=data.exam_date[event]
    elif event in data.college_date:
        event_date=data.college_date[event]

    dataSend = {
            "date" : timemodule.trans(event_date)+" ("+timemodule.weekday(event_date)+") ",
            "d_day": timemodule.check(event_date)
            }
    return jsonify(dataSend)


@app.route('/holiday',methods=['POST'])
def holiday():
    sort_holiday=sorted(data.holiday.items(),key=lambda x: x[1])
    for i in range(len(sort_holiday)):
        if sort_holiday[i][1]>datetime.datetime.now():
            datasend={
                "name": sort_holiday[i][0],
                "date": timemodule.trans(sort_holiday[i][1])+" ("+timemodule.weekday(sort_holiday[i][1])+") ",
                "d_day":timemodule.check(sort_holiday[i][1])
                }
            return jsonify(datasend)

    datasend={
            "Error": "error"}
    return jsonify(datasend)

#셔틀버스 안내

#출근버스
@app.route('/bus_1_1',methods=['POST'])
def bus_1_1():
    with open('json/data_1_go.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

@app.route('/bus_1_1_location',methods=['POST'])
def bus_1_1_location():
    with open('json/data_1_go_location.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)
# 퇴근버스
@app.route('/bus_1_2',methods=['POST'])
def bus_1_2():
    with open('json/data_1_out.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

@app.route('/bus_1_2_location',methods=['POST'])
def bus_1_2_location():
    with open('json/data_1_out_location.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

# 김천구미
@app.route('/bus_2_1',methods=['POST'])
def bus_2_1():
    with open('json/data_2_1.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

@app.route('/bus_2_1_location',methods=['POST'])
def bus_2_1_location():
    with open('json/data_2_1_location.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

# 대곡
@app.route('/bus_2_2',methods=['POST'])
def bus_2_2():
    with open('json/data_2_2.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

@app.route('/bus_2_2_location',methods=['POST'])
def bus_2_2_location():
    with open('json/data_2_2_location.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

# 테크노
@app.route('/bus_2_3',methods=['POST'])
def bus_2_3():
    with open('json/data_2_3.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)

@app.route('/bus_2_3_location',methods=['POST'])
def bus_2_3_location():
    with open('json/data_2_3_location.json', 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)





if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
