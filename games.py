n=int(input())
a=[]
b=[]
for i in range(n):
   x,y =input().split()
   a.append(int(x))
   b.append(int(y))
count=0
for i in range(n):
        count=count+b.count(a[i])
print(count)