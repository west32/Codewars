# import math
# def add_binary(a,b):
#     sum= a + b
#     binary=""
#     divide= None
#     while divide != 0:
#         divide = int(sum//2)
#         modulo = int(sum%2)
#         sum = divide
#         binary += str(modulo)
#     return binary[::-1]

# def add_binary(a,b):
#     sum= a + b
#     binary=""
#     temporary_list=[]
#     divide= None
#     while divide != 0:
#         divide = int(sum/2)
#         modulo = int(sum%2)
#         sum = divide
#         temporary_list.append(modulo)
#         # binary += str(modulo)
#     temporary_list.reverse()
#     for element in temporary_list:
#         binary+=(str(element))
#     return binary
#
# #
# def add_binary(a,b):
#     divide= int((a+b)//2)
#     binary = str(int((a+b)%2))
#     if divide == 1:
#         return (binary +"1")
#     else:
#         return binary + add_binary(a/2,b/2)
# print(add_binary(2,2))

# def add_binary(a, b):
#     return format(a + b, 'b')

# def add_binary(a,b):
#     return f"{a + b:b}"

# add_binary(7,7)
#
#
#
#
#

