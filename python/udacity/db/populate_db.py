from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Address, Base, Employee, MenuItem, Restaurant


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

my_first_restaurant = Restaurant(name='Pizza Palace')
session.add(my_first_restaurant)
session.commit()

cheese_pizza = MenuItem(
    name='Cheese Pizza',
    description='Made with all natural ingredients and fresh mozzarella',
    course='Entree',
    price='$8.99',
    restuarant=my_first_restaurant)
session.add(cheese_pizza)
session.commit()

new_employee = Employee(name='Rebecca Allen')
session.add(new_employee)
session.commit()

rebecca_address = Address(
    street='512 Sycamore Rd', zip='02001', employee=new_employee)
session.add(rebecca_address)
session.commit()


# verify:
rest_test = session.query(Restaurant).first()
print(rest_test.name)
