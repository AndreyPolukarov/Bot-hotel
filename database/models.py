from peewee import *
from datetime import datetime

# TODO: пока не очень понимаю как добавлять в таблицу информацию(User( инфа ).save) не добавляются

db = SqliteDatabase("info_hotel.db")

# Создали класс, чтобы наследовать от него все таблицы базы данных
class BaseModel(Model):
    class Meta:
        database = db

class InfoHotel(BaseModel):
    # В классе описываем таблицу в базе данных
    class Meta:
        db_table = 'Hotels'
    command = CharField()
    hotel_id = IntegerField()
    hotel_name = CharField()
    address = CharField()
    distance = IntegerField()
    price = IntegerField()



class History(BaseModel):
    # В классе описываем таблицу в базе данных
    class Meta:
        db_table = 'History'
    history = ForeignKeyField(InfoHotel)



db.create_tables([InfoHotel, History])



#Подсказка:
# Для того чтобы создать таблицы, можно просто обратится к классу
# User.create_table()
# Метод "create" сразу сохраняет изменение в базе данных
#  и делать коммиты или применять "save" не нужно
# User.create(name='Вася', telegram_id=111)
# User.select().where(User.telegram_id == 111 and User.name == 'Вася')