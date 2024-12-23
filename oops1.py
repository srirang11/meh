# Define 2 numerical datatype variables as static and design a basic calc using class and object
class calc:

    def add(self,a,b):
        print("sum:",a+b)
    def sub(self,a,b):
        print("difference:",a-b)
    def mul(self,a,b):
        print("product:",a*b)
    def div(self,a,b):
        print("quotient:",a/b)
    def exp(self,a,b):
        print(a,"^",b,":",a**b) 
cal=calc()
a=int(input())
b=int(input())
cal.add(a,b)
cal.sub(a,b)
cal.mul(a,b)
cal.div(a,b)
cal.exp(a,b)

