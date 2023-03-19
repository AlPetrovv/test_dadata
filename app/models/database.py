from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from errors.user_error import DBError

DATABASE_NAME = 'dadata.db'  # sqlite
try:
    engine = create_engine(f'sqlite:///{DATABASE_NAME}')  # connect to db

    session = Session(bind=engine)
except Exception as e:
    print(DBError(e))
