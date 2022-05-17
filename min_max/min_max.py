def min_max(lst):
  return [min(lst), max(lst)]


acc = ((1, 123, 1, 1510.0), (2, 456, 2, -510.0), (3, 789, 3, 556.0))

for element in acc:
  print (f" account_id: {element[0]}, account_number: {element[1]}, id_person: {element[2]} balance: {element[3]}, ")