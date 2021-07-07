#print min and max digit in num
#1234
#max=4
#min=1
n=int(input())
min=9
max=0
while(n):
    r=n%10
    if r>max:
        max=r
    elif r<min:
        min=r
    n=n//10
print("max",max)
print("min",min)
