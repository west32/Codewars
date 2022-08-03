def positive_sum(arr):
    sum = 0
    for element in arr:
        if element > 0:
            sum += element
    return sum

# # lub
# def positive_sum(arr):
#     return sum(x for x in arr if x > 0)