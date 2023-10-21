x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])

# 재귀

x=int(input())
dp={1:0}
def rec(n):
    if n in dp.keys():
        return dp[n]
    if (n%3==0) and (n%2==0):
        dp[n]=min(rec(n//3)+1, rec(n//2)+1)
    elif n%3==0:
        dp[n]=min(rec(n//3)+1, rec(n-1)+1)
    elif n%2==0:
        dp[n]=min(rec(n//2)+1, rec(n-1)+1)
    else:
        dp[n]=rec(n-1)+1
    return dp[n]
print(rec(x))