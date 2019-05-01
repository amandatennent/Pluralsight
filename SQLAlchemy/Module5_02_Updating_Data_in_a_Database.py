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


# Update One Record
query = db.update(Post).where(Post.Id == 3).values(ViewCount=1)
result = connection.execute(query)
post_query = my_session.query(Post).filter(Post.Id == 3)

print("ID = {}. View Count = {}. Title = {}.".format(post_query.one().Id,
                                                     post_query.one().ViewCount,
                                                     post_query.one().Title))

# Update all records
query = db.update(Post).values(ViewCount=Post.ViewCount+50)
result = connection.execute(query)
post_query = my_session.query(Post)

for each_post in post_query.all():
    print("ID = {}. View Count = {}. Title = {}.".format(each_post.Id, each_post.ViewCount, each_post.Title))

# Update as an object
my_post = my_session.query(Post).filter(Post.Id == 3).one()
print(my_post.Title)
my_post.Title = 'Modified Post'
my_session.commit()
