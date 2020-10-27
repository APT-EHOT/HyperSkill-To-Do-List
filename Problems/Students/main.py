class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = name[0] + last_name + birth_year


new_name = input()
new_last_name = input()
new_birth_year = input()
student = Student(new_name, new_last_name, new_birth_year)
print(student.id)
