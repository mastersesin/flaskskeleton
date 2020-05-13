from flask import Flask
from flask_cors import CORS
import redis
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
CORS(app)
cache_db = redis.Redis(host='10.10.10.10')
app.config['SECRET_KEY'] = 'trantrongtyckiuzk4ever!@#!!!@@##!*&%^$$#$'
app.config['SITE_ID'] = '3068432376c0c2d957a0bdc9cff202e7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ckiuzk4ever!@#@10.5.5.10:5432/possystem'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)
Base = declarative_base()
from source.classes import sql

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
session.commit()

from source.views import view
