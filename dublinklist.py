class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dublinklist:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_at_start(self,val):
        t=node(val)
        t1=self.head
        if self.head is None:
            self.head=t
            t1=t
            self.tail=t
        else:
            t.next=t1
            t1.prev=t
            self.head=t

    def insert_at_end(self,val):
        t=node(val)
        if self.head is None:
            self.head=t
            self.tail=t
        else:
            self.tail.next=t
            t.prev=self.tail
            self.tail=t

    def insert_in_position(self,val,pos):
        t=node(val)
        t1=self.head
        if pos==0:
            t.next=t1
            t1.prev=t
            self.head=t
            return
        for i in range(pos-1):
            if t1==self.tail:
                print("Invalid position!")
                return
            t1=t1.next
        if t1.next==self.tail:
            self.insert_at_end(val)
            return
        t.next=t1.next
        t1.next.prev=t
        t1.next=t
        t.prev=t1
        
    def delete_head(self):
        self.head=self.head.next
        self.head.prev=None
    
    def delete_tail(self):
        t=self.head
        while t.next!=self.tail:
            t=t.next
        t.next=None
        self.tail=t

    def delete_at_position(self,pos):
        t=self.head
        if pos==0:
            self.delete_head()
            return
        for i in range(pos-1):
            if t==self.tail:
                print("Invalid position!")
                return
            t=t.next
        if t.next==self.tail:
            self.delete_tail()
            return
        t.next=t.next.next
        t.next.prev=t

    def search(self,val):
        if self.head is None:
            print("Empty List")
        else:
            i=0
            t=self.head
            if t.data==val:
                print("Index:",i)
            t=t.next
            i+=1
            while t :
                if t.data==val:
                    print("Index:",i)
                t=t.next
                i+=1

    def reverse(self):
        pre=None
        cur=self.head
        self.tail=cur
        while cur:
            nex=cur.next
            cur.next=pre
            pre=cur
            cur=nex
        self.head=pre
        

    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            t=self.head
            print(t.data,end="")
            t=t.next
            while t :
                print("->",t.data,end=" ")
                t=t.next
            print()
            
o=dublinklist()
for i in range(2,13,2):
    o.insert_at_end(i)
o.display()

n=int(input("No of nodes to be inserted at start: "))
val=list(map(int,input("Values: ").split()))
for i in range(n):
    o.insert_at_start(val[i])
o.display()

n=int(input("No of nodes to be inserted at end: "))
val=list(map(int,input("Values: ").split()))
for i in range(n):
    o.insert_at_end(val[i])
o.display()

pos=int(input("Enter position to insert: "))
val=int(input("Value: "))
o.insert_in_position(val,pos)
o.display()

o.reverse()
o.display()

print("deleting head\n")
o.delete_head()
o.display()

print("deleting tail\n")
o.delete_tail()
o.display()

pos=int(input("delete from position: "))
o.delete_at_position(pos)
o.display()

val=int(input("search: "))
o.search(val)
o.display()