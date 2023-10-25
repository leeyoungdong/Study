n, money = map(int, input().split())

cash = []
for _ in range(n):
    cash.append(int(input()))

d = [10001] * (money+1)

d[0] = 0

for i in range(n):
    for j in range(cash[i], money+1):
        if d[j - cash[i]] != 10001:
            d[j] = min(d[j], d[j - cash[i]] + 1)

if d[money] == 10001:
    print(-1)
else:
    print(d[money])