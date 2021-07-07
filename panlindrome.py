#panlindrome
#n=123
#re=321
#n=rev #panlindrom
#n!=rev #not panlindrom
n=int(input())
t=n
rev=0
while(n):
    r=n%10
    rev=rev*10+r
    n=n//10
if t==rev:
    print("panlindrome")
else:
    print(" not panlindrome")
