from DBMS import DBMS
import re
from datetime import datetime

import pandas as pd
from pandas import DataFrame as df

parList = ['amount','datetime','end','max','min','money','start']

class Query(object):
    def __init__(self,host,ip):
        self.dbms = DBMS(host,ip)

    def get_price_N(self,stock_name,col_name,start_date=None,end_date=None,fields=[]):
        s_datetime = start_date
        e_datetime = end_date

        if s_datetime > e_datetime:
            raise Exception("start time should not be later than end time")

        col = self.dbms.get_col(stock_name, col_name)
        result = col.find({
            'datetime': {'$gte': s_datetime, '$lte': e_datetime}
        })
        d = []
        for m in result:
            del m['_id']
            d.append(m)
        DF = df(d)
        return DF

    def get_price_zeng(self,stock_name,col_name,start_date=None,end_date=None,fields=[]):
        s_datetime = start_date
        e_datetime = end_date

        if s_datetime > e_datetime:
            raise Exception("start time should not be later than end time")

        col = self.dbms.get_col(stock_name, col_name)
        result = col.find({
            'datetime': {'$gte': s_datetime, '$lte': e_datetime}
        })
        d = []
        for m in result:
            del m['_id']
            d.append(m)
        index = ['datetime', 'start', 'end', 'max', 'min', 'amount', 'money']
        DF = df(d).ix[:,index]
        return DF
#start_date and end_date are string format like '2016.2.15.10.45'
#fields is one of []
    def get_price(self,stock_name,col_name,start_date=None,end_date=None,fields=[]):
        s_datetime = start_date
        e_datetime = end_date


        if s_datetime>e_datetime:
            raise Exception("start time should not be later than end time")



        col = self.dbms.get_col(stock_name,col_name)
        result = col.find({
            'datetime' : {'$gte': s_datetime,'$lte':e_datetime}
        })
        d = []
        index =[]
        for m in result:
            del m['_id']
            index.append(m['datetime'])
            if not fields:
                d.append(m)
            else:
                for n in parList :
                    if n not in fields:
                        del m[n]
                d.append(m)

        Df = df(d,index=index)

        return Df


query = Query('219.224.169.45', 12345)
def get_data(stock_name,start_date,end_date,fields=[]):
    a = query.get_price('data',stock_name,start_date,end_date,fields)
    return a

def get_data_normal(stock_name,start_date,end_date,fields=[]):
    a = query.get_price_N('data',stock_name,start_date,end_date,fields)
    return a

def get_data_Daily_original(stock_name,start_date,end_date,fields=[]):
    a = query.get_price_N('data', stock_name, start_date, end_date, fields)

    d = []

#    print a[a['datetime'][0].strftime('%Y-%m-%d')].tail(1)
    for index,row in a.iterrows():
        if(row['datetime'].hour == 9 and row['datetime'].minute == 31):
            d.append(row)

    return df(d).reset_index(drop=True)

def get_data_Daily(stock_name,start_date,end_date,fields=[]):
    str_start_date = start_date.strftime('%Y%m%d') + '0931'
    days = (end_date - start_date).days + 1
    date = pd.date_range(str_start_date, periods=days)
    df = query.get_price_zeng('data', stock_name, start_date, end_date)
    return df[df['datetime'].isin(date)].reset_index(drop=True)

def f(series):
    print series
    return series['datetime'].hour == 15 and series['datetime'].minute == 0

import json
jenc = json.JSONEncoder()

class DateEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,datetime):
            return o.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self,o)
'''
if __name__ == '__main__':
    a =  get_data_Daily('SH600000',datetime(2015, 1, 1),datetime(2015, 6, 1))
    val = a['datetime'].tolist()
    result = {'TradeDate':val}
    print json.dumps(result,cls=DateEncoder)
'''
if __name__ == '__main__':
    start_date = datetime(2015,1,1)
    end_date = datetime(2016,3,3)
    df = get_data_normal('SH600000',start_date,end_date)
    print df.head()
    exit(0)
    query = Query('219.224.169.45', 12345)
    stock_name = 'SH600000'
    start_date = datetime(2015,1,1)
    end_date = datetime(2016,3,3)
    s_date = start_date.strftime('%Y%m%d')+'0931'
    days = (end_date - start_date).days + 1
    date = pd.date_range(s_date, periods=days)
    d = df(date, columns=['date'])
    df = query.get_price_zeng('data', stock_name, start_date, end_date)
    print df[df['datetime'].isin(date)]
    exit(0)