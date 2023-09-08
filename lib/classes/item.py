from sqlalchemy.orm import sessionmaker
from base import engine
from .models import Item, Warehouse

def add_item_function(session, name, description, quantity, price, warehouse_id):
    try:


        # Check if the warehouse with the given ID exists
        warehouse = session.query(Warehouse).filter_by(id=warehouse_id).first()

        if not warehouse:
            print("Error: Warehouse not found.")
            return

        item = Item( name=name, description=description, quantity=quantity, price=price, warehouse=warehouse)
        session.add(item)
        session.commit()

        print(f"Item '{name}' added to the inventory of warehouse '{warehouse.name}'.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Always close the session, whether an error occurred or not
        session.close()


def update_item_quantity(session, name, new_quantity, warehouse):
    try:
        item = session.query(Item).filter_by(name=name, warehouse=warehouse).first()
        if item:
            item.quantity = new_quantity
            session.commit()
            print(f"Quantity for item '{name}' in warehouse '{warehouse.name}' updated to {new_quantity}.")
        else:
            print(f"Item '{name}' not found in the inventory of warehouse '{warehouse.name}'.")
    except Exception as e:
        print(f"Error: {str(e)}")

def view_inventory(session, warehouse):
    try:
        inventory = session.query(Item).filter_by(warehouse=warehouse).all()
        if inventory:
            print(f"Inventory of warehouse '{warehouse.name}':")
            for item in inventory:
                print(f"Name: {item.name}, Description: {item.description}, Quantity: {item.quantity}, Price: ${item.price}")
        else:
            print(f"Inventory of warehouse '{warehouse.name}' is empty.")
    except Exception as e:
        print(f"Error: {str(e)}")
