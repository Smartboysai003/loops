x,y=map(int,input().split())
t,u=x,y
c=0
while(y):
    x,y=y,x%y
    print(x,y)
    c+=1
gcd=x
print("gcd is:",gcd)
lcm=t*u//gcd
print("lcm is :",lcm)
