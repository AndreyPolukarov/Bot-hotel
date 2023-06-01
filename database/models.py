from peewee import *
import pathlib

db_name = pathlib.Path(__file__).parent
db = SqliteDatabase(db_name / "database.db")


# Создали класс, чтобы наследовать от него все таблицы базы данных
class BaseModel(Model):
    class Meta:
        database = db


class Command(BaseModel):
    # В классе описываем таблицу в базе данных
    class Meta:
        db_table = 'Command'

    command = CharField()

class UserCommand(BaseModel):
    # В классе описываем таблицу в базе данных
    class Meta:
        db_table = 'UserCommand'

    num_requests = ForeignKeyField(Command, field='id')
    time = DateTimeField(formats='%Y-%m-%d %H:%M:%S')
    city = CharField()
    hotel_id = IntegerField()
    numbers_hotels = CharField()
    price_min = IntegerField()
    price_max = IntegerField()
    photo_need = CharField()
    photo_count = IntegerField()
    distance_min = IntegerField()
    distance_max = IntegerField()


class InfoHotels(BaseModel):
    class Meta:
        db_table = 'Hotels'

    command_id = ForeignKeyField(Command, field='id')
    hotel_name = CharField()
    address = CharField()
    distance = IntegerField()
    prices = IntegerField()


if __name__ == "__main__":
    db.create_tables([Command, UserCommand, InfoHotels])

# Подсказка:
# Для того чтобы создать таблицы, можно просто обратится к классу
# User.create_table()
# Метод "create" сразу сохраняет изменение в базе данных
#  и делать коммиты или применять "save" не нужно
# User.create(name='Вася', telegram_id=111)
# User.select().where(User.telegram_id == 111 and User.name == 'Вася')
