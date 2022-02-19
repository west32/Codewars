# def alphabet_position(text):
#     alphabet={"a":"1",
#              "b":"2",
#              "c":"3",
#              "d":"4",
#              "e":"5",
#              "f":"6",
#              "g":"7",
#              "h":"8",
#              "i":"9",
#              "j":"10",
#              "k":"11",
#              "l":"12",
#              "m":"13",
#              "n":"14",
#              "o":"15",
#              "p":"16",
#              "q":"17",
#              "r":"18",
#              "s":"19",
#              "t":"20",
#              "u":"21",
#              "v":"22",
#              "w":"23",
#              "x":"24",
#              "y":"25",
#              "z":"26"
#     }
#     output_list=[]
#     output_str=""
#     for letter in text.lower():
#         if letter in alphabet:
#             output_list.append(alphabet[letter])
#
#     return " ".join(output_list)
#
#
# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')