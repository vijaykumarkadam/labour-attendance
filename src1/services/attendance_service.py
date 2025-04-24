from loguru import logger
from datetime import datetime

class Attendanceservice:
    def __init__(self,db_connection):
        self.db_connection = db_connection

    def login_logout(self, labour_id=None, first_name=None, last_name=None):
        cursor = self.db_connection.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_date = datetime.now().strftime('%Y-%m-%d')
        try:
            if labour_id is None:
                if not (first_name and last_name):
                    logger.info("Please provide either 'labour_id' or both 'first_name' and 'last_name'")
                    return

                query = "SELECT id FROM labours1 WHERE lower(first_name) = %s AND lower(last_name) = %s"
                cursor.execute(query, (first_name.lower(), last_name.lower()))
                row = cursor.fetchone()
                if row is None:
                    logger.info("Labour not found.")
                    return
                labour_id = row[0]


            check_query = "SELECT id, start_time, end_time FROM attendance WHERE labours_id = %s AND DATE(start_time) = %s"
            cursor.execute(check_query, (labour_id,current_date))
            result = cursor.fetchone()


            if not result:
                insert_query = "INSERT INTO attendance (labours_id, start_time) VALUES (%s, %s)"
                cursor.execute(insert_query, (labour_id, current_time))
                self.db_connection.commit()
                logger.info(f"Check-in recorded for labour_id {labour_id} at {current_time}.")


            else:
                attendance_id = result[0]
                update_query = "UPDATE attendance SET end_time = %s WHERE id = %s"
                cursor.execute(update_query, (current_time, attendance_id))
                logger.info("Check-out recorded.")
                self.db_connection.commit()
        except Exception as e:
            logger.error(f"Error in login/logout: {e}")
