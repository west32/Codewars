def find_it(seq):
    odd = 0
    for element in seq:
        if seq.count(element) %2 !=0:
          odd = element
    return odd

