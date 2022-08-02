def duplicate_encode(word):
    output_string = ""
    for element in word:
        element = element.lower()
        if word.count(element) > 1:
            output_string += ")"
        elif word.count(element) ==1:
            output_string += "("
    return output_string