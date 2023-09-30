# #간단하게 while / for 문 반복
# n, m, k = list(map(int, input().split()))
# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# secont = data[n-2]

# result = 0

# while 1:
#     for i in range(k):
#         if m==0:
#             break
#         result += first
#         m -=1
    
#     if m == 0:
#         break
#     result += secont
#     m -= 1

# print(result)

# 연산식으로 해결
n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
secont = data[n-2]

count = int(m /(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * secont

print(result)