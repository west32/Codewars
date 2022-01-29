

# def filter_list(l):
#     f=[]
#     for element in l:
#         if isinstance(element,int):
#             f.append(element)
#     return f
# #
def filter_list(l):
  return [i for i in l if not isinstance(i, str)]

