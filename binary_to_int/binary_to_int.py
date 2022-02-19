# #
def binary_array_to_number(arr):
    dec_str = ""
    counter = 0
    decimal_number = 0
    for element in arr:
        dec_str += str(element)
    for element in dec_str[::-1]:
        decimal_number += int(element) * pow(2, counter)
        counter += 1
    return decimal_number

#     dec_str=""
# #     for element in arr:
# #         dec_str += str(element)
# #     return int(dec_str,base=2)
#
# def binary_array_to_number(arr):
#     return int("".join(map(str, arr)), 2)
#
# def binary_array_to_number(arr):
#     return int(''.join(str(a) for a in arr), 2)
#

def binary_to_int(arr):
    dec_str = ""
    counter = 0
    decimal_number = 0
    for element in arr:
        dec_str += str(element)
    for element in dec_str[::-1]:

        decimal_number += int(element) * pow(2,counter)
        counter +=1
    return decimal_number
