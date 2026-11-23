from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    """Declarative base class"""


# Database films_db
sql_engine = create_engine("sqlite:///films_db.sqlite", echo=False)

# Session factory
SessionLocal = sessionmaker(bind=sql_engine)
