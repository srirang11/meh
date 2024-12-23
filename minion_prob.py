s=input()
n=len(s)
c=int(n*(n+1)/2)
vc=0
cc=0
vc=sum([len(s[i:]) for i in range(n) if s[i] in "AEIOU"])
cc=c-vc
if vc<cc:
    print("Stuart",cc)
elif vc==cc:
    print("Draw")
else:
    print("Kevin",vc)