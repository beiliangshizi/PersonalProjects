#coding:utf-8
from flask import json
from flask import render_template,Flask,request
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import mysql


import sys
reload(sys)
sys.setdefaultencoding('utf-8')




app = Flask(__name__)
app.config['SECRET_KEY']='abc'
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:5211314@localhost:3306/test_News"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)

class session(db.Model):
    __tablename__='test'
    content = db.Column(db.String(32), primary_key=True)
    def __repr__(self):
        return '%r' % self.content

@app.route('/',methods=['GET'])
def show():
    # return 'Hello World!'
    newss = []
    Content=session.query.all()
    for i in Content:
        i = str(i).decode('unicode-escape')
        # i = str(i).decode('unicode')
        newss.append(i)
    print newss
    return render_template('GaGaNEWS.html',content=newss)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8888,debug=True)
