# coding: utf-8
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Files(Base):
    __tablename__ = "files"
    id = Column(Text, primary_key=True)
    file_name = Column(Text)
    file_link = Column(Text)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    