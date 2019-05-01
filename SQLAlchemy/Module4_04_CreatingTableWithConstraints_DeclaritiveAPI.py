import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = db.create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/test_postgres_sa')
Base = declarative_base()
metadata = db.MetaData()
connection = engine.connect()
my_session = sessionmaker(bind=engine)()


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


# Create all tables
Base.metadata.create_all(engine)

# Insert data in a statement
users = db.Table('user', metadata, autoload=True, autoload_with=engine)
statement = db.insert(users).values(Name='Xavier Morera')
result = connection.execute(statement)
print(result.rowcount)

# Insert data in a session / as an object
Juli = User(Name='Juli')
Luci = User(Name='Luci')
my_session.add(Juli)
my_session.add(Luci)
my_session.commit()

# Insert data in a statement
posts = db.Table('post', metadata, autoload=True, autoload_with=engine)
statement = db.insert(posts)
values_list = [{'Title': 'Data Science Question', 'OwnerUserId': 1},
               {'Title': 'Big Data Question', 'OwnerUserId': 2}]
result = connection.execute(statement, values_list)

# Print the name of each user in the database
for each_user in my_session.query(User).all():
    print(each_user.Name)

# Print the title of each post in the database
for each_question in my_session.query(Post).all():
    print(each_question.Title)

