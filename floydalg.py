import linklist            

o=linklist.sinlinklist()
for i in range(10,21,10):
    o.insert_at_end(i)

t=o.head
# for i in range(1):
#     t=t.next
o.tail.next=t
o.display()
if o.head==None:
    pass
elif o.head.next==None:
    print("no cycles present")
else:
    i=o.head.next.next
    j=o.head.next
    c=0
    while i!=j:
        if i and j:
            i=i.next.next
            j=j.next
        else:
            c=1
            break
    if c:
        print("no cycles present")
    else:
        j=o.head
        while i!=j:
            i=i.next
            j=j.next
        while i.next!=j:
            i=i.next
        print(f"cycle present at {i.next.data}")
        i.next=None
        print("cycle broken")
o.display()


