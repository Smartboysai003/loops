#product of given number
n=int(input())
p=1
while(n):
    r=n%10
    print(p,'*',r,'=',p*r)
    p*=r
    n=n//10
n+=1
print(p)
