import sqlalchemy as db

# Create table in database
engine = db.create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/test_postgres_sa', echo=True)
connection = engine.connect()
metadata = db.MetaData()

posts = db.Table('posts', metadata,
                 db.Column('Id', db.Integer(), primary_key=True),
                 db.Column('Title', db.String(255), nullable=False),
                 db.Column('ViewCount', db.Integer(), default=1000),
                 db.Column('IsQuestion', db.Boolean(), default=True))
metadata.create_all(engine)
