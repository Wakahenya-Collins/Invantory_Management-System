from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Replace 'sqlite:///your_database_file.db' with the actual path to your SQLite database file.
# You may need to change this URL depending on your database setup (e.g., for PostgreSQL or MySQL).
database_url = 'sqlite:///inventory.db'

# Create an SQLAlchemy Engine object
engine = create_engine(database_url)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()