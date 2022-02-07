# def printer_error(s):
#     counter=0
#     letters_allowed=["n","o","p","r","s","t","u","w","x","v","y","q","z"]
#     for element in s:
#         if element in letters_allowed:
#             counter += 1
#     return "{}/{}".format(counter,len(s))

from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))