# coding:utf-8
from flask import Flask,render_template
import pandas as pd
import sqlalchemy


app=Flask(__name__)

def getData():
    # 连接数据库，sqlalchemy
    engine=sqlalchemy.create_engine('mssql+pymssql://sa:bi.123456@172.22.134.195/ls')
    # 读取数据库的东西
    df=pd.read_sql('select top 10 * from bingan1605',con=engine)
    return df['登记号']

@app.route('/')
def index():
    xx=getData()

    return  xx

if __name__=='__main__':
    app.run(debug=True)



