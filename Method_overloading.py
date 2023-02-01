class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = "Provide atleast two number"
        return s
obj = Myclass()
print(obj.sum(10))


# In python, if a method is written such that
# it can perform more than one task,
# it is called method overloading.