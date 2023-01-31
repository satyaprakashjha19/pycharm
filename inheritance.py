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

# Python example to show the working of multiple
# Inheritance

class Base1():
    # constructor
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")
class Base2():
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")

class Derived(Base1, Base2):
    def __init__(self):

        # Calling / invoking constructor of Base 1
        # and Base 2
        Base1.__init__(self)
        Base2.__init__(self)
        print(Derived)

    def printstrs(self):
        print(self.str1, self.str2)

ob = Derived()
ob.printstrs()


# Multilevel inheritance
# when we have child and grandchild relationship

class Base():
    # constructor
    def __init__(self, name):
        self.name = name
    # Method to get name
    def getName(self):
        return self.name

# Inherited/ Sub class/ child class

class child(Base):
    # constructor
    def __init__(self, name, age):

    # Calling/ invoke Base class
        Base.__init__(self, name)
        self.age = age

    # Method to get age
    def getAge(self):
        return self.age

# Inherited /Sub class/ Grand child class

class Grandchild(child):
    # constructor
    def __init__(self, name, age, address):
        # Invoking child class
        child.__init__(self, name, age)
        self.address = address

    # To get address

    def getAddress(self):
        return self.address

# Driver code

g = Grandchild("Sagar", 25, "India")
print(g.getName(), g.getAge(), g.getAddress())


# Demonstrate Single inheritance

# Parent class
class X():
    def func1(self):
        print("This function is in X class.")
# Derived Class
class Y(X):
    def func2(self):
        print("This function is in Y class")
# Driver code
q = Y()
q.func1()
q.func2()


