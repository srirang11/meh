class stack:
    def __init__(self,s):
        self.stack=[]
        self.size=s
        self.t=-1
        
    def push(self,val):
        if self.t==self.size:
            print("Overflow")
            return
        self.stack.append(val)
        self.t+=1

    def pop(self):
        if self.t==-1:
            return ("Underflow")
        self.t-=1
        return (self.stack.pop())

# c=1
# o=stack(3)
# while c:
#     c=int(input("""Enter stack operation(1-Push,2-Pop,3-Exit): """))
#     match c:
#         case 1:
#             val=int(input("Enter element to push: "))
#             o.push(val)
#         case 2:
#             print(o.pop())
#         case _:
#             break

s=input("Enter Expression: ")
d={"v":")"
   ,"[":"]"
   ,"{":"}"}
inv=0
for i in s:
    if i not in d.keys() and i not in d.values():
        inv+=1
o=stack(len(s))
if inv==0:
    for i in s:
        if o.t==-1:
            o.push(i)
        elif o.stack[o.t] in d.values():
            o.push(i)
        elif d[o.stack[o.t]]== i:
            o.pop()
        else:
            o.push(i)
    if o.t==-1:
        print("Valid!")
    else:
        print("Invalid!")
else:
    print("Invalid input!")


