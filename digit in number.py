#digit in number
#if the digit in the number yes
#if the is digit notin number   no
n=int(input())
d=int(input())
found=0
while(n):
    r=n%10
    if r==d:
        found=1
        break
    n=n//10
if found==1:
    print("yes")
else:
    print("no")
