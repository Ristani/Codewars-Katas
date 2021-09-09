def dna_strand(dna):
    result = []
    for c in dna:
        if c == "A":
            result.append("T")
        elif c == "T":
            result.append("A")
        elif c == "C":
            result.append("G")
        elif c == "G":
            result.append("C")
    return "".join(result)
