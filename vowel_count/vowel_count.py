# def get_count(sentence):
#     vowels = "aeiou"
#     count = 0
#     for element in vowels:
#         count += sentence.count(element)
#     return count

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])