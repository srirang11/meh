import queue
len=int(input("Enter size of Queue: "))
q=queue.Queue(maxsize=len)
while True:
    c=int(input("""Enter queue operation(1-Enqueue,2-Dequeue,3-Display,4-Exit): """))
    match c:
        case 1:
            val=int(input("Enter element to push: "))
            q.put(val)
        case 2:
            print(q.get())
        case _:
            break