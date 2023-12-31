def find_min_ids(a):
    n = len(a)

    min_idx = 0

    for i in range(1,n):

        if a[i] < a[min_idx]:
            min_idx = i
    
    return min_idx

def sel_sort(a):
    
    result = []

    while a:

        min_idx = find_min_ids(a)

        value = a.pop(min_idx)

        result.append(value)

    return result

d = [2, 4, 5, 6, 1]

print(sel_sort(d))