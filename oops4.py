class a:
    def __init__(self):
        self._x=1
    def sri(self):
        print("parent class",self._x)

class b(a):
    def srii(self):
        print("child class",self._x)

    
obj=a()
obj1=b()
obj.sri()
print()
obj1.srii()