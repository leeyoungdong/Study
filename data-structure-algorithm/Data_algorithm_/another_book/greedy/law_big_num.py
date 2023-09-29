n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

# n개의 수를 m번 더하여 k번반복

# set(data)

data.sort()
first = data[n-1]
secont = data[n-2]

result = 0

while 1:
    for i in range(k):
        if m==0:
            break
        result += first
        m -=1
    
    if m == 0:
        break
    result += secont
    m -= 1

print(result)