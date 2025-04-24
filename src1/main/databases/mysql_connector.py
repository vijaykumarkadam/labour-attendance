from loguru import logger
import mysql.connector
from src1.main.utility.encrypt_decrypt import decrypt

class Mysqlconnection1:
    _instance = None

    def __init__(self,config):
        if Mysqlconnection1._instance is not None:
            raise Exception("use get_instance() instead of creating  a new object")

        self.config = config
        self.connection = None
        self.connect()
    @classmethod
    def get_instance(cls,config =None):
        if cls._instance is None:
            cls.instance = cls(config)
            return cls.instance

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host =self.config["mysql_database"]["host"],
                                                 user = self.config["mysql_database"]["user"],
                                                 password = decrypt(self.config["mysql_database"]["password"]),
                                                 database = self.config["mysql_database"]["database"])
            logger.info("connection established")
        except Exception as e:
            logger.info("there is error in db connection")
            raise(e)
    def close(self):
        if self.connection.is_connected:
            self.connection.close()
            logger.info("connection closed")

# class Sqlcrudoperation:
#     def __init__(self,connection):
#         self.connection = connection
#     def read_from_sql(self,query,parameter = None):
#         try:
#             cursor = self.connection.cursor()
#             if parameter:
#                 cursor.execute(query, parameter)
#             else:
#                 cursor.execute(query)
#             result = cursor.fetchall()
#             return result
#         except Exception as e:
#             logger.info("error occurred while reading data")
#             raise e
#         finally:
#             if cursor:
#                 cursor.close()
#                 logger.info("cursor close")
#
#     def insert_to_sql(self,query,parameter):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(query,parameter)
#             inserted_id = cursor.lastrowid
#             logger.info(f"record inserted successfully with id : {inserted_id}")
#             return inserted_id
#         except Exception as e:
#             logger.info("error occurred while inserting data")
#             raise e
#         finally:
#             self.connection.commit()
#             if cursor:
#                 cursor.close()
#
#     def delete_from_sql(self,query,parameter):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(query, parameter)
#             logger.info("record deleted successfully")
#         except Exception as e:
#             logger.info("error occurred while delete data")
#             raise e
#         finally:
#             self.connection.commit()
#
#     def update_to_sql(self,query,parameter):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(query,parameter)
#             logger.info("record updated successfully")
#         except Exception as e:
#             logger.info("error occurred during data updated")
#             raise e
#         finally:
#             self.connection.commit()



