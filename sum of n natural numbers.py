#sum of n naural numbers
'''n*(n+1)//2'''
n=int(input())
i=1
sum=0
while i<=n:
    print(sum,'+',i,'=',sum+i)
    sum+=i
    i+=1
print(sum)

