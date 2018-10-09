def int_to_bin(inte):
    return "{0:b}".format(inte)
def fast_potega(base, fac):
    result = 1
    facbin = int_to_bin(fac)
    for i in range(len(facbin)-1, -1, -1):
        if facbin[i] == "1":
            result = base * result
        base = base * base
    return result