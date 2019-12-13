from flask import Flask,request,jsonify,redirect,url_for
from werkzeug.datastructures import CombinedMultiDict, MultiDict
from flask_cors import *

import json
import pymysql

app = Flask(__name__)
CORS(app, supports_credentials=True)
# 连接数据库
def conn_mysql():
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456Aa',database='hotel',charset='utf8mb4')
    cur = conn.cursor()
    return conn,cur

# 插入数据库
def insert_mysql(sql):
    conn,cur = conn_mysql()
    cur.execute(sql)
    conn.commit()

# 查询数据库
def find_mysql(sql):
    conn,cur = conn_mysql()
    cur.execute(sql)
    result = cur.fetchall()
    list = []
    for i in result:
        list.append(i)
    return list

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/reg',methods=['GET','POST'])
def register():
    if request.method=='POST':
        data= json.loads(request.get_data())
        class1=data['scores']
        id=0
        for i in class1:
            id+=1
            print(id)
            print(i["酒店名称"])
            print(i["用户"])
            print(i["等级"])
            i["入住时间"]=i["入住时间"]+"/1"
            print(i["入住时间"])
            print(i["评价时间"])
            print(i["出差类型"])
            print(i["房型"])
            print(int(i["位置"]))
            print(int(i["设施"]))
            print(int(i["服务"]))
            print(int(i["卫生"]))
            print(i["评价"])
            sql = "insert into hotelrecord values ('%d','%s','%s','%s','%s','%s','%s','%s','%d','%d','%d','%d','%s')" % \
            (id, i["酒店名称"],i["用户"],i["等级"],i["入住时间"],i["评价时间"],i["出差类型"],i["房型"],i["位置"],i["设施"],i["服务"],i["卫生"],i["评价"])
            insert_mysql(sql)
        return request.get_data()
    else:
        return request.get_data()
        # return redirect(url_for("user_list"))

@app.route('/msglsit')
def user_list():
    sql = "select * from user"
    result = find_mysql(sql)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
