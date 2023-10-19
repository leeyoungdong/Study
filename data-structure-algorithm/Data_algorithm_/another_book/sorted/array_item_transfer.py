n, m = map(int, input().split())

a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))

a_array.sort()
b_array.sort(reverse=True)

for i in range(m):
    if a_array[i] < b_array[i]:
        a_array[i], b_array[i] = b_array[i], a_array[i]
    else:
        break

print(sum(a_array))