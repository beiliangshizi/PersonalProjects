#coding=utf-8
from flask_script import Manager
from GaGa_app import app,db
from GaGa_models import News

manager = Manager(app)

@manager.command
def save():
    pass

@manager.command
def query_all():
    news = News.query.all()
    for new in news:
        print new

if __name__ == '__main__':
    manager.run()