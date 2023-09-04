def name_set(a):
    n = len(a)

    for i in range(0, n):
        for j in range(i, n):
            if a[i] == a[j]:
                pass
            else:
                print(a[i],a[j])


name = ['a','b','c']

print(name_set(name))