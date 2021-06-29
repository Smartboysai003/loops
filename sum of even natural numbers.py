#sum of even naural numbers
'''
n=10
2 4 6 8 10
2+4+6+8+10=30
'''
n=int(input())
i=1
sum=0
while i<=n:
    if (i%2==0):
        sum+=i
    i+=1
print(sum)

