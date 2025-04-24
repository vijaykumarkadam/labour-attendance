from loguru import logger
from src1.main.databases.mysql_connector import *
from src1.main.factories.person_factories import Personfactory
from src1.main.utility.encrypt_decrypt import decrypt
from src1.main.models.labour import Labour
from src1.main.models.mishtri import Mishtri
from src1.main.databases.mysql_connector import Mysqlconnection1
import configparser

from src1.services.attendance_service import Attendanceservice
from src1.services.labour_service import Labourservice

config = configparser.ConfigParser()
config.read(r"C:\Users\user\PycharmProjects\PythonProject\src1\resourse\config_file.ini")
db = Mysqlconnection1.get_instance(config)

def create_labour(first_name,last_name,wage,role):
    labour = Personfactory.create_person("labour",first_name=first_name,last_name=last_name,wage=wage,role=role)
    labour_service = Labourservice(db.connection)
    labour_id = labour_service.create_labour(labour)
    return f"labour created with ID : {labour_id}"
def login_logout(labour_id=None,first_name=None,last_name=None):
    attendance_service = Attendanceservice(db.connection)
    attendance_service.login_logout(labour_id,first_name,last_name)
    return "attendance recorded successfully"

#Example
print(create_labour("vijay","kadam",1200,"HR"))
print(login_logout(first_name="vijay",last_name="kadam"))







# def main():
#     try:
#         sql_connection_obj = Mysqlconnection1(config)
#         sql_connection_obj.connect()
#         sql_crud_operation_obj = Sqlcrudoperation(sql_connection_obj.connection)
#         mishtri_obj = Mishtri("raj","yadhav",1500,"manager",sql_crud_operation_obj,"Plumber")
#
#         # labour_obj = Labour("ketan","kadam",1100,"manager")
#         # # labour_obj.save_to_database(sql_crud_operation_obj)
#         # login_obj = Labour.login_logout(sql_crud_operation_obj, first_name="ketan",last_name="kadam")
#
#     except Exception as e:
#         logger.error(f"error in main:{e}")

    # final_read_result = sql_crud_operation_obj.read_from_sql("select * from labours_table")
    # logger.info(f"the data of labours_table is {final_read_result}")
    # sql_connection_obj.close()

    # sql_crud_operation_obj.insert_to_sql("INSERT INTO labours_table (name, role, wages) VALUES (%s, %s, %s)",("prashant","manager",1100,))
    # sql_connection_obj.close()

    # sql_crud_operation_obj.delete_from_sql("delete from labours_table where id = %s", (28,))
    # sql_connection_obj.close()

    # sql_crud_operation_obj.update_to_sql("update labours_table SET name = %s where id = %s",("rohan",29,))
    # sql_connection_obj.close()









# if __name__ == "__main__":
#     main()