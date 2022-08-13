from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from flaskr.mysql_connector import Base, db_session


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    gmt_created = Column(DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False, server_default='')
    firstname = Column(String(100), nullable=False, server_default='')
    lastname = Column(String(100), nullable=False, server_default='')

    def __init__(self, email=None, password=None, firstname=None, lastname=None):
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def insert(self):
        db_session.add(self)
        db_session.commit()
        db_session.remove()

    def queryByEmail(self, email):
        result = self.query.filter_by(email=email).first()
        db_session.remove()
        return result

    def query_by_id(self, user_id):
        result = self.query.filter_by(id=user_id).first()
        db_session.remove()
        return result
