# models.py
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from base import Base,database_url

# Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    warehouses = relationship('Warehouse', back_populates='user')

class Warehouse(Base):
    __tablename__ = 'warehouses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='warehouses')
    
    # Define a relationship to the Item model
    items = relationship('Item', back_populates='warehouse')  # Define the 'items' relationship

    inventory = relationship('Inventory', back_populates='warehouse')

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    warehouse_id = Column(Integer, ForeignKey('warehouses.id'))
    warehouse = relationship("Warehouse", back_populates="items")
    inventory = relationship('Inventory', back_populates='item')



class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    quantity = relationship('Quantity', back_populates='inventory')
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    item = relationship('Item', back_populates='inventory')
    warehouse_id = Column(Integer, ForeignKey('warehouses.id'), nullable=False)
    warehouse = relationship('Warehouse', back_populates='inventory')
engine = create_engine(database_url)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



