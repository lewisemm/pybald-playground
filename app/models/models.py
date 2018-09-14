import sqlalchemy as sqla, ForeignKey as fk

from pybald import context
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(context.config.database_engine_uri, echo=True)
Base = declarative_base()


class User(Base):
    """
    Models the users table.
    """
    __tablename__ = 'users'

    user_id = sqla.Column(sqla.Integer, primary_key=True)
    username = sqla.Column(sqla.String(20))
    password = sqla.Column(sqla.String(255))
    created_at = sqla.Column(sqla.DateTime)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Bucketlist(Base):
    """
    Models the bucketlists table.
    """
    __tablename__ = 'bucketlists'

    b_id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(255))
    created_at = sqla.Column(sqla.DateTime)
    last_modified = sqla.Column(sqla.DateTime)
    user_id = sqla.Column(sqla.Integer, fk('users.user_id'))
    user = relationship("User", back_populates="bucketlists")

    def __repr__(self):
        return '<Bucketlist: {}>'.format(self.name)


class Item(Base):
    """
    Models the items table.
    """
    __tablename__ = 'items'

    item_id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(255))

    completed = sqla.Column(sqla.Boolean)

    created_at = sqla.Column(sqla.DateTime)
    last_modified = sqla.Column(sqla.DateTime)
    bucketlist_id = sqla.Column(sqla.Integer, fk('bucketlists.b_id'))
    bucketlist = relationship("Bucketlist", back_populates="items")

    def __repr__(self):
        return '<Item: {}>'.format(self.name)
