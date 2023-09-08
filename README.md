# Inventory Management System

The Inventory Management System is a comprehensive command-line application that enables users to efficiently manage their inventory, warehouses, items, and users. This system is designed to streamline inventory tracking and management processes.

## Table of Contents

-Features
-Getting Started
  -Prerequisites
  -Installation
-Usage
   -Command Line Interface (CLI)
   -Commands
     -User Management
     -Warehouse Management
     -Item Management
     -Inventory Management
-Contributing
-License

### Features

User Management:

Add new users.
List all users.
Change user roles.

Warehouse Management:

Add new warehouses.
Remove warehouses.
Assign managers to warehouses.

Item Management:

Add new items to warehouses.
Update item details.
Remove items from warehouses.

Inventory Management:

Track and view inventory levels.
Update item quantities in warehouses.
View inventory for all warehouses.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following prerequisites:

Python 3.6 or later installed.
An SQLite database or another supported database system.
Installation
Clone the repository:

```bash
Copy code
git clone https://github.com/yourusername/inventory-management-system.git
```

Change to the project directory:

```bash
Copy code
cd inventory-management-system
Create a virtual environment (optional but recommended):
```

```bash
Copy code
python -m venv venv
Activate the virtual environment (if created):
```

On Windows:

```bash
Copy code
venv\Scripts\activate
On macOS and Linux:
```

```bash
Copy code
source venv/bin/activate
Install the project dependencies:
```

```bash
Copy code
pip install -r requirements.txt
Configure the database:
```

Edit the config.py file to set your database URL. By default, it uses SQLite.
Create the database tables:

```bash
Copy code
python create_tables.py
Usage
Command Line Interface (CLI)
Run the main application:
```

```bash
Copy code
python main.py
You will be presented with a command-line interface (CLI) that allows you to interact with the Inventory Management System.
```

Commands
User Management
add_user: Add a new user.
list_users: List all users.
change_user_role: Change the role of a user.
Warehouse Management
add_warehouse: Add a new warehouse.
remove_warehouse: Remove a warehouse.
assign_manager: Assign a manager to a warehouse.
Item Management
add_item: Add a new item to a warehouse.
update_item: Update item details.
remove_item: Remove an item from a warehouse.
Inventory Management
view_inventory: View inventory levels for all warehouses.
update_quantity: Update the quantity of an item in a warehouse.
Contributing

## Contributions to this project are welcome! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Implement your changes and thoroughly test them.
Commit your changes and create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.