# To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
#
# data =  [(45, 12),(55,21),(19, -2),(104, 20)]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

# def open_or_senior(data):
#     output=[]
#     senior= "Senior"
#     open= "Open"
#     for element in data:
#         if element[0] >= 55 and element[1] >7:
#             output.append(senior)
#         else:
#             output.append(open)
#     return output



def open_or_senior(data):
    return ["Senior" if age>=55 and handicap >7 else "Open" for (age,handicap) in data]


