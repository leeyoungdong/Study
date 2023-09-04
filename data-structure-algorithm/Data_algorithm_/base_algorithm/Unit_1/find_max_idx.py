def find_max(a):
    n = len(a)
    max_v = a[0]

    for i in range(1, n):
        if a[i] > max_v:
            max_v = i
    
    return max_v

v = [3,626,23,43,243,1233,123]

print(find_max(v))