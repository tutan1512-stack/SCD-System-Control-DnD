from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(f'sqlite:///database.db',echo=True)

# не дает упасть программе во время обращения к закрытой сессии после комита
session_orm = sessionmaker(bind=engine, expire_on_commit=False)

# Этот файл отвечает за хранение всех информационных структур необходимые
# для макроконтроля ГМ над игрой по системе "Imprizil"

# Абстрактный класс
class Base(DeclarativeBase):
    pass