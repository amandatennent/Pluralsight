import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

# Create database
engine = db.create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/postgres')
session = sessionmaker(bind=engine)()
session.connection().connection.set_isolation_level(0)
session.execute('CREATE DATABASE test_postgres_sa')
session.connection().connection.set_isolation_level(1)
