n=int(input())
c=0
while (n!=1):
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    c+=1
    print(n,end=" ")
print()
print("count",c)
