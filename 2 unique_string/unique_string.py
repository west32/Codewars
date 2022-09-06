# def find_uniq(arr):
#     unique = None
#     list = []
#
#     for x in (arr):
#         for element in x:
#             list.append(element)
#             if list.count(element) == 1:
#                 unique = element
#
#     for element in arr:
#         if unique in element:
#             return element


def find_uniq(arr):
    if set(arr[0].lower()) == set(arr[1].lower()):
        majority_set = set(arr[0].lower())
    elif set(arr[0].lower()) == set(arr[2].lower()):
        majority_set = set(arr[0].lower())
    else:
        majority_set = set(arr[1].lower())

    for string in arr:
        if set(string.lower()) != majority_set:
            return string