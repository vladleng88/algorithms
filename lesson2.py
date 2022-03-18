n = int(input())
listt = list(map(int, input().split()))
k = int(input())
result = []
summ = 0
for i in range(k):
    summ += listt[i]
result.append(summ/k)
for i in range(1,n-k+1):
    summ -= listt[i-1]
    summ += listt[i+k-1]
    result.append(summ / k)
print(' '.join(map(str, result)))


gen = (i*2 for i in listt)
print(sum(gen))
