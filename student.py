class Student:
    school="akirachix"
    def __init__(self,first_name,last_name,age,country):
       self.first_name=first_name
       self.last_name=last_name
       self.age=age 
       self.country=country 
    def greeting(self):
         return f"Hello {self.full_name}from{self.country},welcome to{self.school} "
        #  return f"Hello {self.full_name} your initials is {self.initial} and you were born in{self.year_of_birth} "

    def full_name(self): 
            return f"{self.first_name} {self.last_name}" 

    def year_of_birth(self):

            return  f"2022-{self.age}"   

    def initial(self):
            return f"{self.first_name[0]} {self.last_name[0]}"
