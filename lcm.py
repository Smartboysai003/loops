#lcm
a,b=map (int, input().split())
if b>a:
    a,b=b,a
j=b
c=0
while(True):
    if j%a==0 and j%b==0:
        print("lcm",j)
        break
    c+=1
    j+=1
