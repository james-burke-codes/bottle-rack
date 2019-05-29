import builtins
import json

from sqlalchemy import inspect
from sqlalchemy import Table, Sequence, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class List(Base):

    __tablename__ = 'list'
    __table_args__ = {'schema': 'list'}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    done = Column(Boolean, nullable=True, default=False)

    def __init__(self, name, done=False):
        self.name = name
        self.done = done

    def __unicode__(self):
        return u'{self.name}'.format(self=self)

    def as_dict(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}