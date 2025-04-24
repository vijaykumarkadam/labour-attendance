from loguru import logger
class Labourservice:
    def __init__(self,db_connection):
        self.db_connection = db_connection

    def create_labour(self, labour):
        cursor = self.db_connection.cursor()

        # Step 1: Check if the labour already exists based on email
        check_query = "SELECT id FROM labours1 WHERE email = %s"
        cursor.execute(check_query, (labour.email,))
        existing = cursor.fetchone()

        if existing:
            logger.info("Labour with email %s already exists.", labour.email)
            return existing[0]  # return the existing ID

        # Step 2: Insert new labour if not exists
        insert_query = """
        INSERT INTO labours1 (first_name, last_name, wages, role, email) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            labour.first_name,
            labour.last_name,
            labour.wage,
            labour.role,
            labour.email
        ))

        self.db_connection.commit()
        logger.info("Labour added successfully.")
        return cursor.lastrowid
