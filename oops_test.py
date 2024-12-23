class goat:
    x=2018
    def platgame(self):
        print("Celeste")
        print("inside method",self.x)
    def metrogame(self):
        type="metroidvania"
        print("Hollow Knight")
        print("Genre",type)

obj=goat()
obj.platgame()
obj.metrogame()
print("outside class",obj.x)