def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
if (is_prime(n)):
    print("prime")
else:
    print("not prime")
while(n):
    r=n%10
    print(r)
    n=n%10
    if r==2 or r==3 or r==5 or r==7 or r==9:
        print("mega")
    else:
        print("not mega")
