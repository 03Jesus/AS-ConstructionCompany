from database.db_session import localSession


def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()
