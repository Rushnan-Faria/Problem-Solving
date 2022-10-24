n=int(input())
c=0
while(n!=0):
    if n>=100:
        t=int(n/100)
        n=n%100
        c=c+t
    elif n>=20:
        t=int(n/20)
        n=n%20
        c=c+t
    elif n>=10:
        t=int(n/10)
        n=n%10
        c=c+t
    elif n>=5:
        t=int(n/5)
        n=n%5
        c=c+t
    elif n>=1:
        t=int(n/1)
        n=n%1
        c=c+t
print(c)
    
