def base_graph(g, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

fr_info = {
    '1': ['2', '3'],
    '2': ['1', '4','5'],
    '3': ['1'],
    '4': ['2'],
    '5': ['2'],

}

base_graph(fr_info, '1')
print()
base_graph(fr_info, '3')