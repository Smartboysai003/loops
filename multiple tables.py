#tables for two range
n=int(input("enter the starting table  "))
s=int(input("enter the ending table  "))
r=int(input("enter upto what range "))
for i in range(n,s+1):
    for j in range(1,r+1):
        print(i,'*',j,'=',i*j)
