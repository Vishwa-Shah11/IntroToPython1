from dateutil.parser import parse

p1 = input()
dob1 = parse(input())
p2 = input()
dob2 = parse(input())

young = ''

if (dob1 > dob2):
  young = p1
elif (dob1 < dob2):
  young = p2
elif (dob1 == dob2):
  young = young.lower()
  if (p1[0] > p2[0]):
    young = p2
  elif (p1[0] < p2[0]):
    young = p1

print(young)