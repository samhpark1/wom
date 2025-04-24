from .Base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

print(type(Base))

class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
