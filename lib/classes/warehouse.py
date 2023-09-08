from .models import User, Warehouse, Item, Inventory
from base import Session
import click

def add_warehouse(name, location, manager_id):
    session = Session()
    manager = session.query(User).filter_by(id=manager_id).first()

    if not manager:
        click.echo(f"User with ID {manager_id} not found.")
        session.close()
        return

    warehouse = Warehouse(name=name, location=location, user=manager)  # Use 'user' instead of 'manager'
    session.add(warehouse)
    session.commit()
    session.close()
    click.echo(f"Warehouse '{name}' added successfully.")




# Function to remove a warehouse by ID
def remove_warehouse(warehouse_id):
    session = Session()
    warehouse = session.query(Warehouse).filter_by(id=warehouse_id).first()
    if not warehouse:
        session.close()
        return None  # Warehouse not found

    session.delete(warehouse)
    session.commit()
    session.close()
    return warehouse

# Function to assign a manager to a warehouse
def assign_manager(user_id, warehouse_id):
    session = Session()
    manager = session.query(User).filter_by(id=user_id, role='manager').first()
    if not manager:
        session.close()
        return None  # Manager not found

    warehouse = session.query(Warehouse).filter_by(id=warehouse_id).first()
    if not warehouse:
        session.close()
        return None  # Warehouse not found

    warehouse.user = manager
    session.commit()
    session.close()
    return warehouse