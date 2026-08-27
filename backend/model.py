from sqlalchemy import create_engine, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

engine = create_engine(f'sqlite:///',echo=False)

# не дает упасть программе во время обращения к закрытой сессии после комита
Session = sessionmaker(bind=engine, expire_on_commit=False)

# Этот файл отвечает за хранение всех информационных структур необходимые
# для макроконтроля ГМ над игрой по системе "Imprizil"

# Абстрактный класс
class Base(DeclarativeBase):
    pass

class Character(Base):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primatu_key = True)
    #--------------------------------
    name: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(20)) # внешний ключ
    fraction: Mapped[str] = mapped_column(String(20)) # внешний ключ
    #--------------------------------
    health: Mapped[int] = mapped_column(Integer())
    hit: Mapped[int] = mapped_column(Integer())
    stress: Mapped[int] = mapped_column(Integer())
    lassitude: Mapped[int] = mapped_column(Integer())
    #--------------------------------
    armor: Mapped[str] = mapped_column(ForeignKey('armor')) # внешний ключ
    weapon: Mapped[str] = mapped_column(String(30))
    #--------------------------------
    power: Mapped[int] = mapped_column(Integer())
    agility: Mapped[int] = mapped_column(Integer())
    intelligence: Mapped[int] = mapped_column(Integer())
    volition: Mapped[int] = mapped_column(Integer())
    #--------------------------------


class Armor(Base):
    __tablename__ = 'armor'
    id: Mapped[int] = mapped_column(primary_key = True)
    #--------------------------------
    name: Mapped[int] = mapped_column(Integer()) # название брони
    armor_point: Mapped[int] = mapped_column(Integer()) # КЗ, определяет уровень защиты для попадания
    armor: Mapped[int] = mapped_column(Integer()) # определяет дайс защиты
    armor_type: Mapped[int] = mapped_column(Integer()) # определяет игнорируемый вид урона
    weigth: Mapped[int] = mapped_column(Integer()) # определяет тяжесть брони
    #--------------------------------
    description: Mapped[str] = mapped_column(String(60))



Base.metadata.create_all(engine)