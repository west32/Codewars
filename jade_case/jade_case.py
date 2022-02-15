# def to_jaden_case(string:str):
#     input_str = ''
#     for index,element in enumerate(string.split(" ")):
#         input_str += element.capitalize()
#         input_str += " "
#     return input_str[:-1]

def to_jaden_case(string):
    return " ".join(w.capitalize() for w in string.split())