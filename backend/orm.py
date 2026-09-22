from sqlalchemy import select
from backend.database import  session_orm
from backend.model import Base

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def create_object(session, Model, **kwargs):
    objects = Model(**kwargs) # создаем объект класса с нашими переменными
    session.add(objects)
    session.commit()
    session.refresh(objects)
    return objects

def delete_object(session, Model, attribute, name_attribute):
    session.query(Model).filter(Model.attribute == name_attribute)
    
