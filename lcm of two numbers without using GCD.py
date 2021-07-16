#lcm of two numbers without using GCD
x,y=map(int,input().split())
i=1
while(y*i%x!=0):
    i+=1
print("lcm is:",y*i)
