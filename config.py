from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#Add your connection string
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/blog'

SQLALCHEMY_TRACK_MODIFICATIONS = True
