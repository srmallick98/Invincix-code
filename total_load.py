def total_load(n):
    if (n <= 0):
        return 0

    count = [0] * (n + 1)
    count[1] = 1

    load = count[0] + count[1]

    # Add remaining terms
    for i in range(2, n + 1):
        count[i] = count[i - 1] + count[i - 2]
        load = load + count[i]

    return load


n = 5
print("Total load received at the end : ", total_load(n))