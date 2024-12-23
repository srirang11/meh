class cqueue:
    def __init__(self,s):
        self.q=[[0]]*s
        self.size=s
        self.f=-1
        self.r=-1
        
    def push(self,val):
        if self.f==-1:
            self.f+=1
            self.r+=1
            self.q[self.r]=(val)
            return ("\0")
        elif (self.r+1)%self.size==self.f:
            return ("Overflow")
        else:
            self.r=(self.r+1)%self.size
            self.q[self.r]=(val)
            return ("\0")

    def pop(self):
        if self.f==-1:
            print("Underflow")
            return ("")
        elif self.r==self.f:
            l=self.q[self.f]
            self.q[self.f]=[0]
            self.f=-1
            self.r=-1
            return l
        else:
            l=self.q[self.f]
            self.q[self.f]=[0]
            self.f=(self.f+1)%self.size
            return l
    
    def display(self):
        d=[]
        for i in self.q:
            if i !=[0]:
                d.append(i)
        print(d)
    
len=int(input("Enter size of Circular Queue: "))
o=cqueue(len)
while True:
    c=int(input("""Enter queue operation(1-Enqueue,2-Dequeue,3-Display,4-Exit): """))
    match c:
        case 1:
            val=int(input("Enter element to enqueue: "))
            print(o.push(val))

        case 2:
            print(o.pop())
        case 3:
            o.display()
        case _:
            break
