# from loguru import logger
# from datetime import datetime
#
#
#
#
#
#     def __save_to_database(self,sql_crud_operation_obj):
#         try:
#             query = f"SELECT id FROM labours1 WHERE lower(first_name) = %s AND lower(last_name) = %s"
#             result = sql_crud_operation_obj.read_from_sql(query,(self.first_name.lower(), self.last_name.lower()))
#
#             if result:
#                 labour_id = result[0][0]
#                 logger.info(f"labour already exit with id :{labour_id}")
#                 return labour_id
#         except Exception as e:
#             logger.error(f"error while read id is exit or not:{e}")
#             raise e
#         try:
#             insert_query = "INSERT INTO labours1(first_name, last_name, wages, role, email) VALUES (%s, %s, %s, %s, %s)"
#             inserted_id = sql_crud_operation_obj.insert_to_sql(
#                 insert_query,
#                 (self.first_name, self.last_name, self.wage, self.role,self.email)
#             )
#             logger.info(f"New labour added with ID: {inserted_id}")
#             return inserted_id
#         except Exception as e:
#             logger.error(f"error occured while inserting data:{e}")
#             raise e
#
#     @staticmethod
#     def login_logout(sql_crud_operation_obj, labour_id=None, first_name=None, last_name=None):
#         try:
#             if labour_id is None:
#                 if not (first_name and last_name):
#                     logger.info("Please provide either 'labour_id' or both 'first_name' and 'last_name'")
#                     return
#
#                 query = "SELECT id FROM labours1 WHERE lower(first_name) = %s AND lower(last_name) = %s"
#                 result = sql_crud_operation_obj.read_from_sql(query, (first_name.lower(), last_name.lower()))
#                 if not result:
#                     logger.error("Labour not found.")
#                     return
#                 labour_id = result[0][0]
#                 logger.info(f"Found labour with ID: {labour_id}")
#
#
#
#             check_query = "SELECT id, start_time, end_time FROM attendance WHERE labours_id = %s AND DATE(start_time) = %s"
#             result = sql_crud_operation_obj.read_from_sql(check_query, (labour_id, current_date))
#
#
#             if not result:
#                 insert_query = "INSERT INTO attendance (labours_id, start_time) VALUES (%s, %s)"
#                 sql_crud_operation_obj.insert_to_sql(insert_query, (labour_id, current_time))
#                 logger.info("Check-in recorded.")
#             else:
#                 attendance_id = result[0][0]
#                 update_query = "UPDATE attendance SET end_time = %s WHERE id = %s"
#                 sql_crud_operation_obj.update_to_sql(update_query, (current_time, attendance_id))
#                 logger.info("Check-out recorded.")
#         except Exception as e:
#             logger.error(f"Error in login_logout: {e}")
#
#
#
#
#
#
#
#
#
