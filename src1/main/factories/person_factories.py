from src1.main.models.labour import Labour
from src1.main.models.mishtri import Mishtri
from loguru import logger
class Personfactory:
    @staticmethod
    def create_person(person_type, **kwargs):
        if person_type.lower() == "labour":
            return Labour(kwargs["first_name"], kwargs["last_name"], kwargs["wage"], kwargs["role"])

        elif person_type.lower() == "mistri":
            return Mishtri(kwargs["first_name"], kwargs["last_name"], kwargs["wage"], kwargs["role"])
        else:
            raise ValueError(f"invalid person type:{person_type}")