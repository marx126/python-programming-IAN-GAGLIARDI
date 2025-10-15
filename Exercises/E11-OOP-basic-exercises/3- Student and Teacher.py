# Student and Teacher
from person import Person
class Student(Person):
    def __init__(self, name, age, email):
        super().__init__(name, age, email)
    
    def study(self):
        return f"study...study...study...more studying"

    def say_hello(self):
        return f"Yo, I am a student, my name is {self.name}, I am {self.age} years old, my email address is {self.email}"
    
class Teacher(Person):
    def __init__(self, name, age, email):
        super().__init__(name, age, email)
    
    def teach(self):
        return f"teach...teach...teach...more teaching"
    
teacher = Teacher("Pernilla", 32, "pernilla@gmail.com") 

student = Student("Karl", 25, "karl@gmail.com")

print(teacher.teach())
print(teacher.say_hello())

print(student.study())
print(student.say_hello())