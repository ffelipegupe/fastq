#!/usr/bin/python3
from models.base import BaseModel
from models.store import Store
from models.food import Food
from models.drink import Drink
from models.order import Order
from models import storage
from models.confirmation import Confirmation

my_store = Store(name="JV")
my_store.save()


my_food = Food(price=4000, store_id=my_store.id, name="Dona")
my_food.save()

my_drink = Drink(price=5000, store_id=my_store.id, name="Cafe")
my_drink.save()


my_order = Order(order_number=1, drink_id=my_drink.id, store_id=my_store.id,
                 user_name="Juan")
my_order.save()
all_order = storage.all(Order)

my_confirmation = Confirmation(store_id=my_store.id, order_id=my_order.id,
                               order_number=3, status="In Progress")
my_confirmation.save()

#print(my_order)

#print(my_store)

#print(my_drink)

#print(my_food)

# Link order with one food/drink
my_order.drinks.append(my_drink)
my_order.foods.append(my_food)

storage.save()
print(all_order)
