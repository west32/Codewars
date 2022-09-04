def find_uniq(arr):
    for x in set(arr):
        print(set(arr))
        if arr.count(x) == 1: return x

