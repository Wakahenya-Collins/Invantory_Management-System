import click
import sys
from cli import cli
from classes.user import add_user, list_users, change_user_role
from classes.warehouse import add_warehouse, remove_warehouse, assign_manager
from classes.item import  view_inventory, add_item_function

@click.command()
def main():
    user_name = input("Enter your name: ")
    click.echo(f"Hello, {user_name}! Welcome to the Inventory Management System.")
    click.echo("You can use the following commands:")
    click.echo("1. To manage users, use 'add_user', 'list_users', and 'change_user_role' commands.")
    click.echo("2. To manage warehouses, use 'add_warehouse', 'remove_warehouse', and 'assign_manager' commands.")
    click.echo("3. To manage items and inventory, use 'add_item', 'update_quantity', and 'view_inventory' commands.")
    click.echo("Use 'python main.py <command> --help' for specific command usage details.")
    click.echo("Type 'exit' to quit the program.")

    while True:
        user_input = input("Enter a command or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break  # Exit the program
        else:
            # Split the user input into words and execute the command
            user_input_parts = user_input.split()
            if user_input_parts:
                command = user_input_parts[0]
                arguments = user_input_parts[1:]
                execute_command(command, arguments)

def execute_command(command, arguments):
    try:
        if command == 'add_user':
            # Handle the 'add_user' command
            name = input("User name: ")
            role = input("User role: ")
            add_user(name, role)  # Assuming you have a function for adding users
            click.echo(f"User '{name}' with role '{role}' added successfully.")
        elif command == 'list_users':
            # Handle the 'list_users' command
            users = list_users()  # Assuming you have a function for listing users
            click.echo("{:<5} {:<20} {:<10}".format("ID", "Name", "Role"))
            for user in users:
                click.echo("{:<5} {:<20} {:<10}".format(user.id, user.name, user.role))
        elif command == 'change_user_role':
            # Handle the 'change_user_role' command
            user_name = input("User name: ")
            new_role = input("New user role: ")
            change_user_role(user_name, new_role)  # Assuming you have a function for changing user roles
            click.echo(f"User '{user_name}' role updated to '{new_role}' successfully.")

        elif command == 'add_warehouse':
            # Handle the 'add_warehouse' command
            name = input("Warehouse name: ")
            location = input("Warehouse location: ")
            user_id = int(input("User ID of the manager: "))  # Assuming the user enters the manager's ID
            add_warehouse(name, location, user_id)  # Assuming you have a function for adding warehouses
            click.echo(f"Warehouse '{name}' added successfully.")
        elif command == 'remove_warehouse':
            # Handle the 'remove_warehouse' command
            warehouse_id = int(input("Warehouse ID to remove: "))
            remove_warehouse(warehouse_id)  # Assuming you have a function for removing warehouses
            click.echo(f"Warehouse with ID {warehouse_id} removed successfully.")
        elif command == 'assign_manager':
            # Handle the 'assign_manager' command
            warehouse_id = int(input("Warehouse ID to assign a manager to: "))
            user_id = int(input("User ID of the manager to assign: "))
            assign_manager(warehouse_id, user_id)  # Assuming you have a function for assigning managers
            click.echo(f"Manager assigned to Warehouse ID {warehouse_id} successfully.")
        elif command == 'add_item':
            # Handle the 'add_item' command
            name = input("Item name: ")
            description = input("Item description: ")
            quantity = int(input("Item quantity: "))
            price = float(input("Item price: "))
            warehouse_id = int(input("Warehouse ID: "))
            add_item_function(name, description, quantity, price, warehouse_id)  # Call the add_item function
            click.echo(f"Item '{name}' added successfully.")
        elif command == 'view_inventory':
            # Handle the 'view_inventory' command
            view_inventory()
        # Add similar logic for other commands...
        elif command == 'exit':
            click.echo("Exiting the program.")
            return
        else:
            click.echo(f"Invalid command: {command}. Please try again.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

if __name__ == '__main__':
    main()

