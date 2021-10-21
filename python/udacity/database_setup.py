import sys

from sqlalchemy import Column, create_engine, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()








## file final
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
