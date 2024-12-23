#Implementation of queue
class queue:
    def __init__(self,s):
        self.q=[]
        self.size=s
        self.t=-1
        
    def push(self,val):
        if self.t==self.size:
            print("Overflow")
            return
        self.q.append(val)
        self.t+=1

    def pop(self):
        if self.t==-1:
            return ("Underflow")
        self.t-=1
        return (self.q.pop(0))
    
    def display(self):
        print(self.q)
    
len=int(input("Enter size of Queue: "))
o=queue(len-1)
while True:
    c=int(input("""Enter queue operation(1-Enqueue,2-Dequeue,3-Display,4-Exit): """))
    match c:
        case 1:
            val=int(input("Enter element to enqueue: "))
            o.push(val)
        case 2:
            print(o.pop())
        case 3:
            o.display()
        case _:
            break

