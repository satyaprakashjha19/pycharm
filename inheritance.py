# Creating a Parent Class
# creating a Person class with Display methods.

class Person:
    # constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)

emp = Person("Satyam", 102)  # An object of person
emp.Display()

# creating a child class
"""Here Emp is another class
which is going to inherit the
properties of the Person class(base class)."""

class Emp(Person):
    def print(self):
        print("Emp class called")
Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# calling child class function
Emp_details.print()


# A python program of inheritance

class Person1():
    # constructor
    def __init__(self, name):
        self. name = name
    # To get name
    def getname(self):
        return self.name
    # To check if this person is an employee
    def isemployee(self):
        return False

# Inherited or subclass

class Employee(Person1):
    # Here we return true
    def isemployee(self):
        return True

emp = Person1("Geek1")  # object of Person
print(emp.getname(), emp.isemployee())

emp = Employee("Geek2")  # object of employee
print(emp.getname(), emp.isemployee())


# Demonstrate how parent constructor called

# parent class

class Person2():

    # Constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    # For Display
    def display(self):
        print(self.name)
        print(self.idnumber)

# child class

class Employeez(Person2):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

    # Invoking the __init__ of parent class
        Person2.__init__(self, name, idnumber)

a = Employeez("Rahul", 885522, 20000, "Intern")
a.display()

