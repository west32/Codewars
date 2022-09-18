def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u", ]
    letter_list = string_.split()
    new_string = []
    for element in letter_list:
        new_word = ""
        for letter in element:

            if letter.lower() not in vowels:
                new_word += letter

        new_string.append(new_word)
    return " ".join(new_string)
