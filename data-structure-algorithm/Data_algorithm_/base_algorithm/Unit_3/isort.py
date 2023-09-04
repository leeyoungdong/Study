def find_ins_dix(r, v):

    for i in range(0, len(r)):

        if v < r[i]:
            return i
        
    return len(r)

def ins_sort(a):
    result = []

    while a:

        value = a.pop(0)

        ins_idx = find_ins_dix(result, value)
        
        result.insert(ins_idx, value)

    return result


d = [2, 4, 5, 6, 1]

print(ins_sort(d))