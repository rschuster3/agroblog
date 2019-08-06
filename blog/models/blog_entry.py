import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy import String, Integer, LargeBinary
from sqlalchemy.dialects.postgresql import TEXT

from blog.models import Base
from utils import alchemy


class BlogEntry(Base):
    blog_id = Column(Integer, primary_key=True)
    title = Column(String(150))
    author = Column(String(50))
    tagline = Column(String(150))
    body = Column(TEXT)
    header_image_url = Column(String(255))
    published = Column(Boolean)
    published_date = Column(DateTime(), default=func.now())


    def __init__(self, *args, **kwargs):
        if kwargs and kwargs.get('published'):
            published = kwargs.get('published')
            kwargs['published_date'] = datetime.datetime.now()

        super(BlogEntry, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<BlogEntry(title='%s', author='%s', blog_id='%s')>" % (
            self.title,
            self.author,
            self.blog_id
        )

    @classmethod
    def get_id(cls):
        return BlogEntry.blog_id
