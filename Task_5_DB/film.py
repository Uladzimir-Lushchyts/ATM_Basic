import logging

from sqlalchemy import String, delete, select, Column, Integer
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import Session
from database import Base
from db_error import DBError
from db_operation import DBOperation

logger = logging.getLogger(__name__)


class Film(Base):

    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)

    def __repr__(self):
        return f"id={self.id}, title={self.title}, director={self.director}, year={self.release_year}"


def films_commit(operation: DBOperation, session: Session):
    try:
        session.commit()
    except (IntegrityError, OperationalError) as e:
        session.rollback()
        raise DBError(f"{type(e).__name__} during {operation.value} on \"films\": {e}") from e
    except Exception as e:
        session.rollback()
        raise DBError(f"Unexpected error during {operation.value} on \"films\": {e}") from e


def add_film(title: str, director: str, release_year: int, session: Session):
    film = Film(title=title, director=director, release_year=release_year)
    session.add(film)

    try:
        films_commit(DBOperation.ADD, session)
    except DBError as e:
        logger.error(f"Error adding film {title}: {e}")
    else:
        logger.info(f"Added a row to the \"films\" table: {film}")


def show_all_films(session: Session):
    all_films = session.scalars(select(Film)).all()

    if all_films:
        for film in all_films:
            print(film)
    else:
        print("The table is empty")


def delete_all_films(session: Session):
    session.execute(delete(Film))

    try:
        films_commit(DBOperation.DELETE, session)
    except DBError as e:
        logger.error(f"Error deleting all films: {e}")
    else:
        logger.info("Deleted all films from the \"films\" table")


def query_by_title(session: Session, title: str):
    return session.query(Film).filter_by(title=title).first()

def update_film(session: Session, film: Film, **fields):

    try:

        for name, value in fields.items():
            if name not in ("title", "director", "release_year"):
                raise ValueError(f"ValueError. Unknown film field: {name}")
            setattr(film, name, value)

            films_commit(DBOperation.UPDATE, session)

    except DBError as e:
        logger.error(f"Error updating film {film} with {fields}: {e}")
    except ValueError as e:
        logger.error(e)
    else:
        logger.info(f"Updated film: {film}")
