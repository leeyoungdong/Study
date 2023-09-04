def sum_n(n):
    s = 0

    for i in range(1, n+1):
        s = s + i
    return s

if __name__ == "__main__":
    print(sum_n(100))