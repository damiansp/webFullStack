from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Address, Base, Employee, MenuItem, Restaurant


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

employees = session.query(Employee).all()
for e in employees:
    print(e.name)
