# class op:
#     def add(self,a,b):
#         print(a+b)
# obj=op()
# obj.add(4,5)
# obj.add("race","car")/

# class op:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c=0):
#         print(a+b+c)
# obj=op()
# obj1=op()
# obj.add(4,5)
# obj1.add(6,7,8)

# from multipledispatch import dispatch
# class example:
#    @dispatch(int, int)
#    def add(self, a, b):
#       x = a+b
#       return x
#    @dispatch(int, int, int)
#    def add(self, a, b, c):
#       x = a+b+c
#       return x

# obj = example()

# print (obj.add(10,20,30))
# print (obj.add(10,20))