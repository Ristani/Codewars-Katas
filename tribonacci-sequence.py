def tribonacci(signature, n):
    res = signature[:n]
    for _ in range(n - 3):
        res.append(sum(res[-3:]))
    return res
