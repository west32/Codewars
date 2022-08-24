def unique_in_order(iterable):

    output = []
    previous = None
    for element in iterable:
        if element != previous:
            output.append(element)
            previous = element
    return output