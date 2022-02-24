# def square_digits(num):
#     input_string = ""
#     for element in str(num):
#         input_string += str(int(element) ** 2)
#     output_int = int(input_string)
#     return output_int

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

