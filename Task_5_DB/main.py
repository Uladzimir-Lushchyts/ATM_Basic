import logging

from log_setup import setup_logging
from database import Base, SessionLocal, sql_engine
from film import add_film, delete_all_films, query_by_title, show_all_films, update_film

logger = logging.getLogger(__name__)

def main() -> None:
    # Create the database and the "films" table
    Base.metadata.create_all(sql_engine)

    with SessionLocal() as session:
        # Add 3 films
        add_film("Film 1", "Director 1", 1999, session)
        add_film("Film 2", "Director 2", 2000, session)
        add_film("Film 3", "Director 3", 2021, session)

        # Update 1 film
        film = query_by_title(session, "Film 3")
        if film:
            update_film(session, film, title="Film 2_new")
        else:
            print("No films found")

        # Print the table
        show_all_films(session)

        # Delete all records
        delete_all_films(session)


if __name__ == "__main__":
    setup_logging()
    main()
