from sqlalchemy import Enum, String
from enum import Enum as PyEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


class UserRole(PyEnum):
    admin = "admin"
    user = "user"
    guest = "guest"


class User(Base):
    username: Mapped[str] = mapped_column(String(15), unique=True)
    password: Mapped[str]
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.guest)


# class Token(Base):
#     access_token: Mapped[str]
#     token_type: Mapped[str]
#
#
# class TokenData(Base):
#     username: Mapped[str] | None = mapped_column(default=None)
