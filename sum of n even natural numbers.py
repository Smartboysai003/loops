#sum of n even natural numbers
n=int(input())
i=1
sum=0
while i<=n:
    if i%2==0:
        sum+=i
        print(i)
i+=1
    
