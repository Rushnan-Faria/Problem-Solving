def checkComposite(x):
    r=False
    for i in range(2, int(x/2)+1):
         if (x % i) == 0:
            r=True
            break
    return r
			 
n=int(input())
if(n%2==0):
    x=int(n/2)
else:
    x=int(n/2)+1
while(1):
    y=n-x
    print(x,y)
    c1=checkComposite(x)
    if(c1==True):
       c2=checkComposite(y)
       if(c2==True):
        print(x,y)
        break
    x=x+1