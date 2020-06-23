# Primitives
name = 'John'
age = 37
country = 'USA'
birth_date = 1967-12-12

# Class data object
class Person:
    def __init__(self, name, age, country, birth_date):
        self._name = name
        self._age = age
        self._country = country
        self._birth_date = birth_date
    def hi(self):
        print("Hello", self._name)

print(name, age, country, birth_date)
student = Person("John Rambo", 37, "USA", 1967-12-12)
print(student._name, student._age, student.hi())
instructor = Person("Bruce Wayne", 43, "USA", 1964-12-12)
print(instructor._name, instructor._age, instructor.hi())
