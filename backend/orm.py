from sqlalchemy import select
from backend.database import  session_orm
from backend.model import Base

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

#
def save(objet):
    session = session_orm
    session.add(objet)
    session.commit()
    session.refresh(objet)
    return  objet

# функция для добавления элемента класса
def insert_data(
        **kwargs # словарь объекта, в котором передаем характеристики
    ):
        save(**kwargs)

