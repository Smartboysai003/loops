'''
n=1234
e=24
e**2=24**2=576
0=13
o**2=169
'''
n=int(input())
rev=0
while(n):
    r=n%10
    rev=rev*10+r
    n=n//10
e=0
o=0
while(rev):
    r=rev%10
    if r%2==0:
        e=e*10+r
    else:
        o=o*10+r
    rev=rev//10
print(e)
print(e**2)
print(o)
print(o**2)

