import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types.choice import ChoiceType
from typing import TypeAlias

from models.database import engine

Base: TypeAlias = declarative_base()


class User(Base):
    LANGUAGES = [
        ('en', "en"),
        ('ru', "ru")
    ]
    __tablename__ = "user"
    id: int = sa.Column(sa.Integer(), primary_key=True, autoincrement=True)
    token: str = sa.Column(sa.String(250), nullable=False, unique=True)
    language = sa.Column(ChoiceType(LANGUAGES), nullable=False)

    def __str__(self):
        return f"User {self.id}"


Base.metadata.create_all(engine)
