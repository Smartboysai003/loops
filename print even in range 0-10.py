#print even numbers between range
n=int(input())
m=int(input())
while n<=m:
    if n%2==0:
        print(n,end=" ")
    n+=1
