from sqlalchemy import (
    Column, Table, PrimaryKeyConstraint, DateTime, func,
    inspect
)
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.ext.declarative import as_declarative

from utils import alchemy


@as_declarative()
class BaseModel(object):
    """
    Base model that tells us when an instance is created/modified, allows
    us to do some basic operaions (like converting data to a json dict),
    and sets correct table info of child models.
    """
    created = Column(DateTime, default=func.now())
    modified = Column(DateTime, default=func.now(), onupdate=func.now())

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.set_fields(kwargs)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @classmethod
    def __table_cls__(cls, *arg, **kw):
        for obj in arg[1:]:
            if (isinstance(obj, Column) and obj.primary_key) or isinstance(
                obj, PrimaryKeyConstraint
            ):
                return Table(*arg, **kw)

        return None

    @classmethod
    def find_one(cls, session, id):
        return session.query(cls).filter(cls.get_id() == id).one()

    @classmethod
    def find_update(cls, session, id, args):
        return (
            session.query(cls)
            .filter(cls.get_id() == id)
            .update(args, synchronize_session=False)
        )

    @classmethod
    def get_id(cls):
        pass

    def to_dict(self):
        d = {}
        mapper = inspect(self)
        for column in mapper.attrs:
            d[column.key] = getattr(self, column.key)

        return d

    def set_fields(self, new_data):
        existing_data = self.to_dict()
        for k, v in new_data.iteritems():
            if k in existing_data:
                setattr(self, k, v)

        self.update(new_data)


Base = declarative_base(cls=BaseModel)
