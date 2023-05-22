# from typing import Dict, List, TypeVar
# from database.models import db
# from database.models import BaseModel
#
#
# T = TypeVar('T')
# def _store_date(db: db, model: T, *data: List[Dict]) -> None:
#     with db.atonic():
#         model.insert_many(*data).execute()
#
# def _retrieve_all_data(db: db, model: T, *colunns: BaseModel):
#     with db.atonic():
#         response = model.select(*colunns)
#
#     return response
#
# class CODEInterface():
#     @staticmethod
#     def create():
#         return _store_date
#
#     @staticmethod
#     def retrieve():
#         return _retrieve_all_data
#
# if __name__ == "main":
#     _store_date()
#     _retrieve_all_data()
#     CODEInterface()

