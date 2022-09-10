def nb_year(p0, percent, aug, p):
    n = 0
    while p0 < p:
        n += 1
        per = percent * 0.01
        p0 += int(p0 *per) + aug

    return n

