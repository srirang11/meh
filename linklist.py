class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class sinlinklist:
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
            self.head=t
            t1=t

    def insert_at_end(self,val):
        t=node(val)
        if self.head is None:
            self.head=t
            self.tail=t
        else:
            self.tail.next=t
            self.tail=t

    def insert_in_position(self,val,pos):
        t=node(val)
        t1=self.head
        if pos==0:
            t.next=t1
            self.head=t
        else:
            for i in range(pos-1):
                if t1.next==None:
                    print("Invalid position!")
                    return
                t1=t1.next
            t.next=t1.next
            t1.next=t
        
    def delete_head(self):
        self.head=self.head.next
    
    def delete_tail(self):
        t=self.head
        while t.next!=self.tail:
            t=t.next
        t.next=None

    def delete_at_position(self,pos):
        t=self.head
        for i in range(pos-1):
                t=t.next
        t.next=t.next.next

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
        prev=None
        cur=self.head
        self.tail=cur
        while cur:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        self.head=prev
        

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
            
# o=sinlinklist()
# for i in range(2,13,2):
#     o.insert_at_end(i)
# o.display()

# n=int(input("No of nodes to be inserted at start: "))
# val=list(map(int,input("Values: ").split()))
# for i in range(n):
#     o.insert_at_start(val[i])
# o.display()

# n=int(input("No of nodes to be inserted at end: "))
# val=list(map(int,input("Values: ").split()))
# for i in range(n):
#     o.insert_at_end(val[i])
# o.display()

# pos=int(input("Enter position to insert: "))
# val=int(input("Value: "))
# o.insert_in_position(val,pos)
# o.display()

# o.reverse()
# o.display()

# print("deleting head\n")
# o.delete_head()
# o.display()
# print("deleting tail\n")
# o.delete_tail()
# o.display()
# pos=int(input("delete from position: "))
# o.delete_at_position(pos)
# o.display()
# val=int(input("search: "))
# o.search(val)
# o.display()