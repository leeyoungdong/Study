# binary_search
def binary_search(source, target, start, end):
    while start<=end:
        mid = (start+ end) // 2
        if source[mid] == target:
            return mid
        elif source[mid] > target:
            return binary_search(source, target, start, mid-1)
        elif source[mid] < target:
            return binary_search(source, target, mid+1, end)
        
n = int(input())
total = list(map(int, input().split()))
m = int(input())
asking = list(map(int, input().split()))

total.sort()

for i in asking:
    result = binary_search(total, i, 0, n-1)
    if result != None:
        print('yes', end= ' ')
    else:
        print('no', end= ' ')

# 계수 정렬
n = int(input())
total = [0] * 1000001

for i in input().split():
    total[int(i)] = 1

m = int(input())
asking = list(map(int, input().split()))

for i in asking:
    if total[i] == 1:
        print('yes', end= ' ')
    else:
        print('no', end= ' ')

# 집합자료
n = int(input())
total = list(map(int, input().split()))
m = int(input())
asking = list(map(int, input().split()))

for i in asking:
    if i in total:
        print('yes', end= ' ')
    else:
        print('no', end= ' ')