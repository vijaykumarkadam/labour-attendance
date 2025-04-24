from loguru import logger

class person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name + '.' + self.last_name + '@gmail.com'

    def print_details(self):
        return f"person first_name is {self.first_name} and last_name is {self.last_name}"

    def to_dict(self):
        return {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email" : self.email
        }