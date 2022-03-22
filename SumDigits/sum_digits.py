def sum_digits(number):
    number = abs(number)
    output_int = 0
    for element in str(number):
        output_int += int(element)
    return output_int

# def sumDigits(number):
#     return sum(int(d) for d in str(abs(number)))
    # return int(str(abs(number))[0]) + int(str(abs(number))[1])







