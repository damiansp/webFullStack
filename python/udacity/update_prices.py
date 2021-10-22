from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Address, Base, Employee, MenuItem, Restaurant


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

veggie_burgers = session.query(MenuItem).filter_by(name='Veggie Burger')
for vb in veggie_burgers:
    print(f'{vb.id} {vb.restaurant.name}: {vb.price}')

urban_veggie_burger = session.query(MenuItem).filter_by(id=9).one()
SALE_PRICE = '$2.99'
urban_veggie_burger.price = SALE_PRICE
session.add(urban_veggie_burger)
session.commit()

for vb in veggie_burgers:
    if vb.price != SALE_PRICE:
        vb.price = SALE_PRICE
        session.add(vb)
session.commit()

# have to requery
veggie_burgers = session.query(MenuItem).filter_by(name='Veggie Burger')
print()
for vb in veggie_burgers:
    print(f'{vb.id} {vb.restaurant.name}: {vb.price}')
