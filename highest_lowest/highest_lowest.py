# def high_and_low(numbers):
#     integers_nums = [int(element) for element in numbers.replace(" ", ",").split(",")]
#     numbers = f"{max(integers_nums)} {min(integers_nums)}"
#
#     return numbers


def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
