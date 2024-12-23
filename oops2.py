class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.id,self.name)
        print(f"hi im {self.name}, my id is {self.id}")
emp1=employee("Peter",213)
emp2=employee("Wade",124)
emp1.display()
emp2.display()

