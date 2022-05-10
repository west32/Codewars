# def count_by(x, n):
#     result = []
#     result.append(x)
#     while len(result) != n:
#         next_val = result[-1] + x
#         result.append(next_val)
#     return result

def count_by(x, n):
    return range(x, x * n + 1, x)