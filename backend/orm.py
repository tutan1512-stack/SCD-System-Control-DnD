from sqlalchemy import select
from backend.model import Base

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

#
def save(session, objet):
    session.add(objet)
    session.commit()
    session.refresh(objet)
    return  objet

# функция для добавления элемента класса
def insert_data(
        session, # сессия в которой мы работаем
        **kwargs # словарь объекта, в котором передаем характеристики
    ):
        save(session, **kwargs)


