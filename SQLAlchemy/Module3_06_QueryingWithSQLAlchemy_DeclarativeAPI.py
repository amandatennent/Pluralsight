from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/sqlalchemy')

session = sessionmaker()
session.configure(bind=engine)
my_session = session()


class Users(Base):
    __tablename__ = 'users'
    Id = Column(Integer, primary_key=True)
    Reputation = Column(Integer)
    CreationDate = Column(DateTime)
    DisplayName = Column(String(255))
    LastAccessDate = Column(DateTime)
    WebsiteUrl = Column(String(255))
    Location = Column(String(4096))
    AboutMe = Column(String(4096))
    Views = Column(Integer)
    UpVotes = Column(Integer)
    DownVotes = Column(Integer)
    AccountId = Column(Integer)

    def __repr__(self):
        return "<{0} Id: {1} - Name: {2}>".format(self.__class__.__name__, self.Id, self.DisplayName)


print(my_session.query(Users).first())
print(my_session.query(Users).first().DisplayName)

#for each_user in my_session.query(Users):
#    print(each_user)

the_query = my_session.query(Users)
print(the_query)


engine_echo = create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/sqlalchemy', echo=True)
session_echo = sessionmaker(bind=engine_echo)()
session_echo.query(Users).first()
