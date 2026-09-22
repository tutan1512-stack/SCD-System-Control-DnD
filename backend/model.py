from typing import Annotated
from sqlalchemy import MetaData, String, Integer, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from backend.database import Base, engine, session_orm

idtp = Annotated[int, mapped_column(primary_key= True)] # шаблон типа данных для первичных ключей

# базовый класс персонажа
class Character(Base):
    __tablename__ = 'characters'
    id: Mapped[idtp]
    #--------------------------------
    name: Mapped[str] = mapped_column(String(50))
    role_fk: Mapped[int | None] = mapped_column(ForeignKey('role.id')) # внешний ключ
    worldview_fk: Mapped[int | None]=mapped_column(ForeignKey('worldview.id'))
    fraction_fk: Mapped[int | None] = mapped_column(ForeignKey('fractions.id')) # внешний ключ
    location_fk: Mapped[int] = mapped_column(Integer, ForeignKey('locations.id'))
    #--------------------------------
    body_fk:Mapped[int]=mapped_column(Integer, ForeignKey('body.id'))
    #--------------------------------
    inventory_fk:Mapped[int]=mapped_column(ForeignKey('inventories.id'))
    #--------------------------------
    power: Mapped[str] = mapped_column(String(3))
    agility: Mapped[str] = mapped_column(String(3))
    intelligence: Mapped[str] = mapped_column(String(3))
    volition: Mapped[str] = mapped_column(String(3))
    #--------------------------------

    body = relationship('Body', back_populates='character')
    role = relationship('Role', back_populates='character')
    fraction = relationship('Fraction', back_populates='character')
    location = relationship('Location', back_populates='character')

    inventory = relationship('Inventory', back_populates='character')

    def __repr__(self):
        return f'Worldview: {self.id=}: {self.name=}: {self.role_fk=} : {self.worldview_fk=} : {self.fraction_fk=}\
                            : {self.location_fk=} : {self.body_fk=} : {self.inventory_fk=} : {self.power=} : {self.agility=}\
                            : {self.intelligence=} : {self.volition=}'

class Body(Base):
    __tablename__ = 'body'
    id: Mapped[idtp]
    # --------------------------------
    name:Mapped[str]=mapped_column(String(15))
    description:Mapped[str]=mapped_column(String(50))
    # --------------------------------
    health: Mapped[int] = mapped_column(Integer()) #
    hit: Mapped[int] = mapped_column(Integer())
    stress: Mapped[int] = mapped_column(Integer())
    lassitude: Mapped[int] = mapped_column(Integer())

    character = relationship('Character', back_populates='body')

    def __repr__(self):
        return f'Worldview: {self.id=}: {self.name=}: {self.description=} \
                            : {self.health=} : {self.hit=} : {self.stress=} : {self.lassitude=}'

# Класс ролей/классов, за которые будут играть
class Role(Base):
    __tablename__ = 'role'
    id: Mapped[idtp]
    #--------------------------------
    name: Mapped[str] = mapped_column(String(30)) # название роли/класса
    ability_frt: Mapped[int | None] = mapped_column(ForeignKey('ability.id')) # способность
    ability_scd: Mapped[int | None] = mapped_column(ForeignKey('ability.id'))  # способность
    ability_passive: Mapped[int | None] = mapped_column(ForeignKey('ability.id'))  # способность
    #--------------------------------
    description: Mapped[str] = mapped_column(String(150)) # описание роли

    character = relationship('Character', back_populates='role')

    def __repr__(self):
        return f'Worldview: {self.id=}: {self.name=}: {self.description=} : {self.ability_frt=} \
                            : {self.ability_scd=} : {self.ability_passive=}'

# класс фракций позиционирующие в мире
class Fraction(Base):
    __tablename__ = 'fractions'
    id: Mapped[idtp]
    #--------------------------------
    name: Mapped[str] = mapped_column(String(30)) # название фракции
    location_fk: Mapped[int] = mapped_column(ForeignKey('locations.id')) # Локация + внешний ключ
    worldview_fk: Mapped[int | None] = mapped_column(ForeignKey('worldview.id')) # Мировоззрение + внешний ключ
    ability_fk: Mapped[int | None] = mapped_column(ForeignKey('ability.id')) # способность фракции
    #--------------------------------
    description: Mapped[str] = mapped_column(String(150))

    character = relationship('Character', back_populates='fraction')
    worldview = relationship('Worldview', back_populates='fraction')
    ability = relationship('Ability', back_populates= ' fraction')

    def __repr__(self):
        return f'Fraction: {self.id=}: {self.name=}: {self.description=} : {self.location_fk=}\
                            : {self.worldview=} : {self.ability_fk=} '

# мировоззрения персонажей
class Worldview(Base):
    __tablename__='worldview'
    id: Mapped[int] = mapped_column(primary_key=True)
    #--------------------------------
    name: Mapped[str]=mapped_column(String(20)) # название мировоззрения
    description: Mapped[str]=mapped_column(String(150))

    fraction = relationship('Fraction', back_populates='worldview')

    def __repr__(self):
        return f'Worldview: {self.id=}: {self.name=}: {self.description=}'

class Ability(Base):
    __tablename__ = "ability"
    id: Mapped[idtp]
    #--------------------------------
    name:Mapped[str]=mapped_column(String(10))
    distance:Mapped[int]=mapped_column(Integer())
    damage:Mapped[str]=mapped_column(String(3))
    description: Mapped[str]=mapped_column(String(150))

    character = relationship('Character', back_populates='ability')
    fraction = relationship('Fraction', back_populates='ability')

    def __repr__(self):
        return f'Ability: {self.id=}: {self.name=}: {self.description=}: {self.damage=} : {self.distance=}'

# класс для отображения игровых мест
class Location(Base):
    __tablename__ = 'locations'
    id: Mapped[idtp]
    #--------------------------------
    name: Mapped[str]=mapped_column(String(20))
    description: Mapped[str]=mapped_column(String(150))

    character = relationship('Character', back_populates='location')

    def __repr__(self):
        return f'Location: {self.id=}: {self.name=}: {self.description=}'

class Item(Base):
    __tablename__ = 'items'
    id: Mapped[idtp]
    #--------------------------------
    name:Mapped[str]=mapped_column(String(20))

    property:Mapped[str | None]=mapped_column(String(50))
    description:Mapped[str]=mapped_column(String(150))
    weight:Mapped[float]=mapped_column()

    inventory2 = relationship('Inventory', back_populates='item')

    def __repr__(self):
        return f'Items: {self.id=}: {self.name=}: {self.description=}: {self.property=} : {self.weight=}'

class Inventory(Base):
    __tablename__ = 'inventories'
    id: Mapped[idtp]
    #--------------------------------
    character_fk:Mapped[int]=mapped_column(ForeignKey('characters.id'))
    item_fk:Mapped[int]=mapped_column(ForeignKey('items.id'))
    quality: Mapped[int]=mapped_column(Integer)

    character = relationship('Character', back_populates='inventory')
    item = relationship('Item', back_populates='inventory')

    def __repr__(self):
        return f'Inventory: {self.id=}: {self.character_fk=}: {self.item_fk=} : {self.quality=}'

# Класс брони
class Armor(Item):
    __tablename__ = 'armors'
    id: Mapped[int] = mapped_column(ForeignKey('items') , primary_key = True)
    #--------------------------------
    defense: Mapped[int] = mapped_column(Integer()) # КЗ, определяет уровень защиты для попадания
    armor: Mapped[str] = mapped_column(String(3)) # определяет дайс защиты
    type: Mapped[str] = mapped_column(String(15)) # определяет игнорируемый вид урона

    def __repr__(self):
        return f'Weapon: {self.id=}: {self.name=}: {self.description=}: {self.property=} : {self.weight=} : {self.type=} :\
        {self.defense=} : {self.armor=}'

class Weapon(Item):
    __tablename__ = 'weapons'
    id:Mapped[int]=mapped_column(ForeignKey('items'), primary_key=True)
    #--------------------------------
    type:Mapped[str]=mapped_column(String(20))
    distance:Mapped[int]=mapped_column(Integer)
    damage:Mapped[str]=mapped_column(String(3))

    def __repr__(self):
        return f'Weapon: {self.id=}: {self.name=}: {self.description=}: {self.property=} : {self.weight=} : {self.type=} :\
        {self.damage=} : {self.damage=}'



Base.metadata.create_all(engine)



croosbow = Item(id = 1, name = 'Арбалет',description =' добротный Авризильский арбалет', property = 'Зловонный', weight = 15 )


session_orm.add(croosbow)
session_orm.commit()


print(croosbow)