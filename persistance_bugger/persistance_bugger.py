def persistence(n):
    if len(str(n))==1:
        return 0

    n_list = []
    multip = 1
    for element in str(n):
        n_list.append(element)
    for element in n_list:
        multip *= int(element)

    counter = 1
    while len(str(multip))>1:
        n_list.clear()
        counter += 1

        for element in str(multip):
            n_list.append(element)
        multip = 1
        for element in n_list:
            multip *= int(element)


    return(counter)