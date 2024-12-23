def ques(ans):
    global f,m
    if f:
        d={"a":0,"b":0,"c":0,"d":0}
        d[ans]=1
        c=input("\nDo you want to skip this Question(y/n): ")
        if c=="n":
            a=input("\nEnter your answer: ")
            if d[a]:
                print("\nYay, you get 1 mark")
                m+=1
            elif not d[a]:
                print("\nOh no, you lose 1 mark")
                m-=1
            else:
                print("\nInvalid option")
            print(f"\nYou have {m} marks.")
            f=input("\nDo you want to quit(y/n): ")
        elif c=="y":
            print()
    return

f=1
name=input("Name:")
print(f"Hello {name}, welcome to Quiz \n\n")
m=0
print("""What is the game of the year(2024)?
      a)Balatro
      b)Lorelie and the Laser Eyes
      c)Astro Bot
      d)Black Myth Wukong""")
ques("c")
print("""What is my favourite game?
      a)Hollow Knight
      b)Celeste
      c)Astro Bot
      d)Super Mario Oddeyssey""")
ques("b")
print("\nEnd of quiz\n")
print(f"\nYou have {m} marks.")

    
