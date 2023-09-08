# cli.py
from sqlalchemy.orm import sessionmaker
import click
from classes.models import User, Warehouse, Item, Inventory
from classes.user import User
from classes.item import add_item_function
from base import engine, Session

@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', prompt='User name')
@click.option('--role', prompt='User role')
def add_user(name, role):
    session = Session()
    user = User(name=name, role=role)
    session.add(user)
    session.commit()
    session.close()
    click.echo(f"User '{name}' with role '{role}' added successfully.")


@cli.command()
def list_users():
    session = Session()
    users = session.query(User).all()
    click.echo("{:<5} {:<20} {:<10}".format("ID", "Name", "Role"))
    for user in users:
        click.echo("{:<5} {:<20} {:<10}".format(user.id, user.name, user.role))
    session.close()


@cli.command()
@click.option('--name', prompt='User name')
@click.option('--role', prompt='User role')
def change_user_role(name, role):
    session = Session()
    user = session.query(User).filter_by(name=name).first()
    if user:
        user.role = role
        session.commit()
        session.close()
        click.echo(f"User '{name}' role updated to '{role}' successfully.")
    else:
        click.echo(f"User with name '{name}' not found.")

@cli.command()
@click.option('--name', prompt='Warehouse name')
@click.option('--location', prompt='Warehouse location')
@click.option('--user-id', prompt='User ID', type=int)
def add_warehouse(name, location, user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        click.echo(f"User with ID {user_id} not found.")
        session.close()
        return

    warehouse = Warehouse(name=name, location=location, manager=user)
    session.add(warehouse)
    session.commit()
    session.close()
    click.echo(f"Warehouse '{name}' added successfully.")


@cli.command()
@click.option('--warehouse-id', prompt='Warehouse ID', type=int)
@click.option('--manager-id', prompt='Manager ID', type=int)
def assign_manager(warehouse_id, manager_id):
    session = Session()
    warehouse = session.query(Warehouse).filter_by(id=warehouse_id).first()

    if not warehouse:
        click.echo(f"Warehouse with ID {warehouse_id} not found.")
        session.close()
        return

    manager = session.query(User).filter_by(id=manager_id).first()

    if not manager:
        click.echo(f"User with ID {manager_id} not found.")
        session.close()
        return

    warehouse.user = manager
    session.commit()  # Commit the changes to the database
    session.close()
    click.echo(f"Manager assigned to Warehouse ID {warehouse_id} successfully.")

@cli.command()
def add_item():
    try:
        # Create a new session from the sessionmaker
        session = Session()

        name = click.prompt('Enter Item name')
        description = click.prompt('Enter Item description')
        quantity = click.prompt('Enter Item quantity', type=int)
        price = click.prompt('Enter Item price', type=float)
        warehouse_id = click.prompt('Enter Warehouse ID', type=int)

        # Call the add_item_function with the correct argument order
        add_item_function(session, warehouse_id, name, description, quantity, price)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Always close the session, whether an error occurred or not
        session.close()


# def add_item_function(session, name, description, quantity, price, warehouse_id):
#     try:
#         # Check if the warehouse with the given ID exists
#         warehouse = session.query(Warehouse).filter_by(id=warehouse_id).first()

#         if not warehouse:
#             print("Error: Warehouse not found.")
#             return

#         item = Item(name=name, description=description, quantity=quantity, price=price, warehouse=warehouse)
#         session.add(item)
#         session.commit()

#         print(f"Item '{name}' added to the inventory of warehouse '{warehouse.name}'.")
#     except Exception as e:
#         print(f"Error: {str(e)}")



@cli.command()
@click.option('--item-id', prompt='Item ID', type=int)
@click.option('--warehouse-id', prompt='Warehouse ID', type=int)
@click.option('--quantity', prompt='Quantity', type=int)
def update_quantity(item_id, warehouse_id, quantity):
    try:
        # Create a new session from the sessionmaker
        session = Session()

        # Query the warehouse and item
        warehouse = session.query(Warehouse).filter_by(id=warehouse_id).first()
        item = session.query(Item).filter_by(id=item_id).first()

        if not warehouse:
            click.echo(f"Warehouse with ID {warehouse_id} not found.")
            return

        if not item:
            click.echo(f"Item with ID {item_id} not found.")
            return

        # Query the inventory for the item in the warehouse
        inventory = (
            session.query(Inventory)
            .filter_by(warehouse_id=warehouse_id, item_id=item_id)
            .first()
        )

        if not inventory:
            # Create a new inventory entry if it doesn't exist
            inventory = Inventory(warehouse=warehouse, item=item, quantity=quantity)
            session.add(inventory)
        else:
            # Update the quantity if the inventory entry exists
            inventory.quantity = quantity

        session.commit()
        click.echo(f"Quantity for item '{item.name}' in warehouse '{warehouse.name}' updated to {quantity}.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")
    finally:
        # Always close the session, whether an error occurred or not
        session.close()

@cli.command()
def view_inventory():
    try:
        session = Session()
        warehouses = session.query(Warehouse).all()

        for warehouse in warehouses:
            click.echo(f"Warehouse: {warehouse.name}")
            click.echo("{:<15} {:<20} {:<10}".format("Item ID", "Item Name", "Quantity"))
            for inventory in warehouse.inventory:
                click.echo("{:<15} {:<20} {:<10}".format(inventory.item.id, inventory.item.name, inventory.quantity))
            click.echo("\n")

        session.close()
    except Exception as e:
        click.echo(f"Error: {str(e)}")


if __name__ == '__main__':
    cli()
