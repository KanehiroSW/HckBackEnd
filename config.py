import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/osteovisionbd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False