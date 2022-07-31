def is_valid_walk(walk):
    a_axis = 0
    b_axis = 0
    for element in walk:
        if element == "w":
            a_axis -= 1
        elif element == "e":
            a_axis += 1
        elif element == "n":
            b_axis += 1
        elif element == "s":
            b_axis -= 1
    if a_axis == 0 and b_axis == 0 and len(walk) == 10:
        return True
    else:
        return False