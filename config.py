# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('9f87d3b7f4d6ad2d8e8f76f70c9a1b65a1db7f4cb8e9f3e7a9d8f7b6c4a3b291') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = 'postgresql://myuser:mypassword@localhost:5432/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

'''
postgres=# CREATE DATABASE test;
CREATE DATABASE
postgres=# CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE test TO myuser;
GRANT
postgres=# \q
'''
