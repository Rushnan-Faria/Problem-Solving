t=input()
for i in range(int(t)):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if a%b==0:
        print("0")
    elif a<b:
        print(b-a)
    else:
        x=int(a/b)
        print((b*(x+1))-a)
