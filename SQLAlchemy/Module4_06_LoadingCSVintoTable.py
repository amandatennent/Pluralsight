import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Create database
engine = db.create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/postgres')
session = sessionmaker(bind=engine)()
session.connection().connection.set_isolation_level(0)
session.execute('CREATE DATABASE sql_alchemy_csv')
session.connection().connection.set_isolation_level(1)

# Connect to new database
engine = db.create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/sql_alchemy_csv')
connection = engine.connect()

# Read CSV File
with open('tags.csv', 'r') as file:
    tags_df = pd.read_csv(file)

# Save data from CSV file to database
tags_df.to_sql('tags', con=engine)
