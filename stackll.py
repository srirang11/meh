import linklist
o=linklist.sinlinklist()
c=1
while c:
    c=int(input("""Enter stack operation(1-Push,2-Pop,3-Display,4-Exit): """))
    match c:
        case 1:
            val=int(input("Enter element to push: "))
            o.insert_at_start(val)
        case 2:
            print(o.head.data)
            o.delete_head()
        case 3:
            o.reverse()
            o.display()
            o.reverse()
        case _:
            break