import math
def comp(array1, array2):
    result = True
    if array1 is None or array2 is None:
        result = False
    else:
        for element in array1:
            operation = element * element
            if operation not in array2:
                result = False
        for element in array2:
            if math.sqrt(element) not in array1:
                result = False

    return result


