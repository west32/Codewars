def find_uniq(arr):
    unique = None
    list = []

    for x in (arr):
        for element in x:
            list.append(element)
            if list.count(element) == 1:
                unique = element

    for element in arr:
        if unique in element:
            return element




