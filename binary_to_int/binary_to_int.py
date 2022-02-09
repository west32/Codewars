#
# def binary_array_to_number(arr):
#     dec_str=""
#     for element in arr:
#         dec_str += str(element)
#     return int(dec_str,base=2)

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

def binary_array_to_number(arr):
    return int(''.join(str(a) for a in arr), 2)


