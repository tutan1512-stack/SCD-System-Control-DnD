from sqlalchemy import select, delete
from backend.database import  session_orm
from backend.model import Base

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def create_object(session, Model, attribute,**kwargs):
    try:
        objects = Model(**kwargs)  # создаем объект класса с нашими переменными

        found = session.scalar(
            select(Model).where(
                Model.attribute == objects.attribute
            )
        )
        # found Находит существующие записи в бд, если такая запись есть, он ее вернет, иначе None

        if found is None:
            session.add(objects)
            session.commit()
            session.refresh(objects)
            return objects # возвращает результат при вызове

        else:
            print('[>] Ошибка: Объект уже существует')
            return found # если мы нашли объект, то мы его и вернем

    except Exception as e:
        print(f'[!] Ошибка: {type(e).__name__}')
        print(f'[>] Сообщение: {e}')


def delete_object(session, Model, attribute, sample_attribute):
    try:
        objects = session.scalar(
            select(Model).where(
                Model.attribute == sample_attribute
            )
        )

        if objects is not None:
            session.delete(objects)
            session.commit()

        else:
            print('[>] Объекта нет в БД')

    except Exception as e:
        print(f'[!] Ошибка: {type(e).__name__}')
        print(f'[>] Сообщение: {e}')
