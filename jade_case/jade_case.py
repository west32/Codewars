def to_jaden_case(string:str):
    input_str = ''
    for index,element in enumerate(string.split(" ")):
        input_str += element.capitalize()
        if index == [-1]:
            break
        else:
            input_str += " "
    return input_str[:-1]

