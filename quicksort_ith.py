def partition(ar, l, h):
    pivot = ar[h]
    i = l - 1

    for j in range(l, h):
        if ar[j] < pivot:
            i += 1
            ar[i], ar[j] = ar[j], ar[i]

    ar[i + 1], ar[h] = ar[h], ar[i + 1]
    return i + 1

def quickSelect(ar, l, h, i):
    if l < h:
        pi = partition(ar, l, h)

        if pi == i:
            return ar[pi]
        elif pi < i:
            return quickSelect(ar, pi + 1, h, i)
        else:
            return quickSelect(ar, l, pi - 1, i)

    return ar[l]

ar = [112, 45, 47, 233, 119, 226, 40, 22]
n = len(ar)
i = 4

result = quickSelect(ar, 0, n - 1, i)
print(f"The {i}th order statistic is: {result}")
