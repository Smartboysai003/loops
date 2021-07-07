#print the even digit count and odd  digit count
#n=1234
#2 odd digit 2 even digit
n=int(input())
e=0
o=0
while(n):
    r=n%10
    if r%2==0:
        e+=1
    else:
        o+=1
    n=n//10
print('count of even',e)
print('count of odd',o)
