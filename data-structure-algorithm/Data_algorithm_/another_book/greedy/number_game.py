# # min 함수사용
# n, m = list(map(int, input().split()))

# result = 0

# for i in range(n):
#     data = list(map(int, input().split()))
#     min_val = min(data)
#     result = max(result, min_val)

# print(result)

# 2중 for 문
n, m = list(map(int, input().split()))

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_val = 10001
    for a in data:
        min_val = min(min_val,a)
    result = max(result, min_val)

print(result)