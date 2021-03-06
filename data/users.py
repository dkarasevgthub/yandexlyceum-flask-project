import datetime

import sqlalchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):  # таблица пользователей
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    photo = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=False, nullable=True, default='-')
    is_photo = sqlalchemy.Column(sqlalchemy.Boolean,
                                 index=True, unique=False, nullable=True, default=0)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    news = orm.relation("News", back_populates='user')
    accounts = orm.relation("Accounts", back_populates='user')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

