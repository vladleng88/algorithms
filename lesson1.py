n = int(input())
str1 = input().split()
str2 = input().split()
summStr = []
for i in range(n):
    summStr.append(str1[i])
    summStr.append(str2[i])
print(' '.join(summStr))