from contextlib import contextmanager

import logging

from app.config import settings
import app.logger

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger("sqlalchemy.engine")
logger.setLevel(app.logger.level)
for handler in logger.handlers:
    handler.setFormatter(app.logger.formatter)


def open_session():
    database_engine = create_engine(settings.DATABASE_URL)
    session_factory = sessionmaker(bind=database_engine)
    session = scoped_session(session_factory)
    return session


@contextmanager
def create_session():
    session = open_session()
    try:
        yield session
    finally:
        session.close()
