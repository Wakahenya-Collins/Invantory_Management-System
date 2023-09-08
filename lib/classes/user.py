from .models import User, Warehouse, Item, Inventory
from base import Session

def add_user(name, role):
    session = Session()
    user = User(name=name, role=role)
    session.add(user)
    session.commit()
    session.close()
    return user

# Function to list all users
def list_users():
    session = Session()
    users = session.query(User).all()
    session.close()
    return users

def change_user_role(user_name, new_role):
    session = Session()
    user = session.query(User).filter_by(name=user_name).first()

    if user:
        user.role = new_role
        session.commit()
        session.close()
        print(f"User '{user_name}' role updated to '{new_role}'.")
    else:
        print(f"User '{user_name}' not found.")