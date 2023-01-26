# Defining a Function

def disp():
    name = "satyaprakash"
    print(name)

# Calling a function

disp()

def my_funcion():
    print("Hello from a function")
my_funcion()


"""A parameter is the variable listed inside
the parentheses in the function definition.
An argument is the value that is sent to the
function when it is called."""

def Name_function(fname):
    print(fname + " Superheros")

Name_function("Batman")
Name_function("Spiderman")
Name_function("venom")

# Number of Arguments

def full_name(f_name, l_name):
    print(f_name + " " + l_name)

full_name("satyaprakash", "jha")

"""If you do not know how many arguments
that will be passed into your function,
add a * before the parameter name
in the function definition."""

def boys(*kids):
    print("The youngest child is " + kids[0])

boys("harry potter", "Heman", "panther")

# keyword arguments

def kids(child1, child2, child3):
    print("The youngest child is " + child3)
kids(child1= "sonu", child2= "Sagar", child3= "abhijeet")

"""If you do not know how many keyword arguments
that will be passed into your function,
add two asterisk:** before the parameter name
in the function definition."""

def males(**kid):
    print("His last name is " + kid["lname"])
males(fname = "Sonu", lname = "Jha")

# Nested Function

def disp():
    def show():
        print("Show Function")
    print("Disp function")
    show()

disp()

# Return statement
def disp():
    def show():
        return "Show Function "
    result = show() + "Disp function"
    return result

a = disp()
print(a)

# Pass a function as a parameter

def disp(sh):
    print("Disp function " + sh())
def show():
    return "show function"
disp(show)