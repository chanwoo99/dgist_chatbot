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
@app.route('/bus_1_1',methods=['POST'])
def bus_1_1():
    with open(json/data_1_go.json, 'r') as f:
        datasend = json.load(f)
        return jsonify(datasend)




if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080)
