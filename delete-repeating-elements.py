def delete_nth(order,max_e):
    result = []
    occurrences = {}
    for n in order:
        count = occurrences.setdefault(n, 0)
        if count >= max_e:
            continue
        result.append(n)
        occurrences[n] += 1
    return result