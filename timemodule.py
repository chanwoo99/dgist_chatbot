# -*- coding: utf8 -*-

import datetime




def check(to):
    now=datetime.datetime.now()
    diff=to-now
    day=diff.days
    hour=diff.seconds//3600
    minute=(diff.seconds%3600)//60
    second=(diff.seconds%3600)%60

    return str(day)+"일"+str(hour)+"시간"+str(minute)+"분"+str(second)+"초"


def trans(time):
    return str(time.year)+"년"+str(time.month)+"월"+str(time.day)+"일"


def weekday(time):
    weekdata=["월","화","수","목","금","토","일"]
    return weekdata[time.weekday()]
