class Add:
    def result(self, x, y):
        print("Addition:", x+y)

class Multi(Add):
    def result(self, a, b):
        Add.result(self, 30, 20)   # calling parent class method
        print("Multiplication:", a*b)

m = Multi()
m.result(10,20)