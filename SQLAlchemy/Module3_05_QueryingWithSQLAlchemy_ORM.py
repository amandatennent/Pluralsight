from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine
from sqlalchemy.orm import mapper

engine = create_engine('postgresql+psycopg2cffi://sqlalchemyuser:post@localhost:5432/sqlalchemy')

metadata = MetaData()

tags = Table('tags', metadata,
             Column('Id', Integer, primary_key=True),
             Column('Count', Integer),
             Column('ExcerptPostId', Integer),
             Column('TagName', String(255)),
             Column('WikiPostId', Integer))


class Tags(object):
    def __init__(self, Count, ExcerptPostId, tag_name, WikiPostId):
        self.Count = Count
        self.ExcerptPostId = ExcerptPostId
        self.tag_name = tag_name
        self.WikiPostId = WikiPostId


tags_mapper = mapper(Tags, tags)
larger_tags = tags.select(Tags.Count > 1000)
print(type(larger_tags))
print(engine.execute(larger_tags).fetchall())

