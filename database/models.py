import peewee as pw
from datetime import datetime

db = pw.SqliteDatabase("database_hotel.db")
class BaseModel(pw.Model):
    created_at = pw.DateField(default=datetime.now())
    class Meta:
        database = db
class User(BaseModel):
    name = pw.CharField()
    telegram_id = pw.IntegerField()

class History(BaseModel):
    numver = pw.TextField()
    message = pw.TextField()



#Подсказка:
# Для того чтобы создать таблицы, можно просто обратится к классу
# User.create_table()
# Метод "create" сразу сохраняет изменение в базе данных
#  и делать коммиты или применять "save" не нужно
# User.create(name='Вася', telegram_id=111)
# User.select().where(User.telegram_id == 111 and User.name == 'Вася')