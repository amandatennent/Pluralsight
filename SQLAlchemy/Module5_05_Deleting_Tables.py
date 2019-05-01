import sqlalchemy as db

engine = db.create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/test_postgres_sa')
metadata = db.MetaData()
metadata.reflect(bind=engine)

post_table = metadata.tables['post']
post_table.drop(bind=engine)
