from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from config import DB_URI


# Set up scoped sessions (one per web request) to handle
# database communication. Then set up our database engine.
db_session = scoped_session(sessionmaker())
engine = create_engine(DB_URI)


def init_session():
    db_session.configure(bind=engine)
