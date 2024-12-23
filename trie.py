class tnode:
    def __init__(self,c):
        self.data=c
        self.isword=False
        self.next=[]
class trie:
    def __init__(self):
        self.root=[]
    def insert(self,s):
        self.t=None
        c=1
        for j in self.root:
                if s[0]==j.data:
                    self.t=j
                    c=0
        if c:
            self.t=tnode(s[0])
            self.root.append(self.t)
        self.ins2(s[1:])

    def ins2(self,s):
        for i in s:
            c=1
            for j in self.t.next:
                if i==j.data:
                    self.t=j
                    c=0
            if c:
                t=tnode(i)
                self.t.next.append(t)
                self.t=t
        self.t.isword=True  
          
    def check(self,s):
        t=self.root
        for i in range(len(s)-1):
            for j in t:
                if s[i]==j.data:
                    t=j.next
                    break
        c=1
        for j in t:
            if s[-1]==j.data and j.isword:
                print("it is a word")
                c=0
        if c:
            print("it is not a word")

    def complete(self,s):
        t=self.root
        cs=""
        for i in range(len(s)):
            for j in t:
                if s[i]==j.data:
                    t=j.next
                    l=j
                    cs+=j.data
                    break
        if l.isword==True:
            print(cs)
            return
        while t[0].isword==False:
            cs+=t[0].data
            t=t[0].next
        cs+=t[0].data
        print(cs)    

            

        
obj=trie()
s="srirang"
obj.insert(s)
obj.insert("rishikesh")
obj.insert("sathyan")
obj.insert("sathi")
obj.insert("ashina")
obj.insert("reynor")
str=input("Enter name to complete: ")
obj.complete(str)


