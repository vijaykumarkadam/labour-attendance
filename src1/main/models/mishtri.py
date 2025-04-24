from loguru import logger
from src1.main.models.labour import Labour


class Mishtri(Labour):
    def __init__(self,first_name,last_name,wage,role,sql_crud_operation_obj,skill):
        super().__init__(first_name,last_name,wage,role,sql_crud_operation_obj)
        self.skill = skill
        self.__save_to_skill_table()

    def __save_to_skill_table(self):
        insert_query = "INSERT INTO skills (labours_id,skills) VALUES (%s, %s)"
        self.sql_crud_operation_obj.insert_to_sql(insert_query, (self.id, self.skill))

    def to_dict(self):
        data = super().to_dict()
        data.update({"skill":self.skill})
        return data