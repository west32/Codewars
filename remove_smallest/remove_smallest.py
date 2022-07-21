def remove_smallest(numbers):
    new_numbers = numbers.copy()
    if len(numbers) >= 1:
        smallest_one = 999
        for element in new_numbers:
            if element < smallest_one:
                smallest_one = element

        new_numbers.remove(smallest_one)
    return new_numbers


# szybsze rozwiazanie nizej

# def remove_smallest(numbers):
#     a = numbers[:]
#     if a:
#         a.remove(min(a))
#     return a