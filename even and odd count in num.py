#even and odd count
n=int(input())
ec=0
oc=0
while(n):
    r=n%10
    if r%2==0:
        ec+=r
    else:
        oc+=r
    n=n//10
print("even count",ec)
print("odd count",oc)
