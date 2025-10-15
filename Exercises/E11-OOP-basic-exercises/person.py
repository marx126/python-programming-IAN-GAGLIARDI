# Person
import validators

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, (str)):
            raise TypeError("Value must be a string")
        self._name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, (int, float)):
            raise TypeError("Value must be an intiger or float")
        if new_age <= 0:
            raise ValueError("Value must be a positive number")
        self._age = new_age

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        if not isinstance(new_email, (str)):
            raise TypeError("Value must be a string")
        if not validators.email(new_email):
            raise TypeError(f"{new_email} is not a valid email, format must be xxxx@yyyy.zzz")
        self._email = new_email

    def say_hello(self):
        return f"Hi, my name is {self._name}, I am {self._age} years old, my email address is {self._email}"
    
    def __repr__(self):
        return f"Person(name={self._name}, age={self._age}, email={self._email})"

if __name__ == "__main__":
    p = Person("Pernilla", 32, "pernilla@gmail.com") 
    print(p)

    try:
        p = Person("Pernilla", 32, "pernillagmail.com")
    except TypeError as ex:
        print(ex)
    except NameError as ex:
        print(ex)
