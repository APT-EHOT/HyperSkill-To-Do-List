class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, I am {self.name}!'


new_name = input()
person = Person(new_name)
print(person.greet())
