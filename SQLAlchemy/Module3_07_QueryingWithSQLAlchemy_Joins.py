from sqlalchemy.orm import sessionmaker, aliased
#from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine, DateTime, desc
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = db.create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/sqlalchemy')

session = sessionmaker()
session.configure(bind=engine)
my_session = session()


class Users(Base):
    __tablename__ = 'users'
    Id = db.Column(db.Integer, primary_key=True)
    Reputation = db.Column(db.Integer)
    CreationDate = db.Column(db.DateTime)
    DisplayName = db.Column(db.String(255))
    LastAccessDate = db.Column(db.DateTime)
    WebsiteUrl = db.Column(db.String(255))
    Location = db.Column(db.String(4096))
    AboutMe = db.Column(db.String(4096))
    Views = db.Column(db.Integer)
    UpVotes = db.Column(db.Integer)
    DownVotes = db.Column(db.Integer)
    AccountId = db.Column(db.Integer)

    def __repr__(self):
        return "<{0} Id: {1} - Name: {2}>".format(self.__class__.__name__, self.Id, self.DisplayName)


class Posts(Base):
    __tablename__ = 'posts'
    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    ViewCount = db.Column(db.Integer, default=1000)
    PostTypeId = db.Column(db.Integer, default=True)
    OwnerUserId = db.Column(db.Integer)
    __table_args__ = {'extend_existing': True}
    AnswerCount = db.Column(db.Integer)
    ParentId = db.Column(db.Integer)
    Score = db.Column(db.Integer)


# Implicit Join
print(my_session.query(Users, Posts).filter(Users.Id == Posts.OwnerUserId).first())

# Explicit Join
print(my_session.query(Users, Posts).join(Posts, Users.Id == Posts.OwnerUserId).first())

Questions = aliased(Posts)
print(my_session.query(Posts.Id, Questions.Id, Posts.ViewCount, Posts.Score, Questions.Score)
                .filter(Posts.Id == Questions.ParentId)
                .order_by(db.desc(Posts.ViewCount))
                .limit(10)
                .all())
