
for N in range(1, 26):
    step = 1
    cur = 1

    while cur < N:
        cur += (6 * step)
        step += 1

    print(N, step)