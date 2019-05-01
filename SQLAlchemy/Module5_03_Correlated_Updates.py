import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = db.create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/test_postgres_sa')
session = sessionmaker()
session.configure(bind=engine)
my_session = session()
connection = engine.connect()
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())


class Post(Base):
    __tablename__ = 'post'
    Id = db.Column(db.Integer(), primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    ViewCount = db.Column(db.Integer(), default=1000)
    Question = db.Column(db.Boolean(), default=True)
    OwnerUserId = db.Column(db.Integer(), db.schema.ForeignKey('user.Id'), nullable=False)
    User = relationship('User', backref='post')


avg_views = db.select([db.func.avg(Post.ViewCount).label('AverageViews')])
query = db.update(Post).values(ViewCount=avg_views)
result = connection.execute(query)

