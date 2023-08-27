#2020 day 3

input = open('input.txt').read().splitlines()
Xposition = 0
treeCount = 0

for i in input:
  if list(i)[Xposition % len(i)] == "#": treeCount += 1

  Xposition += 3 

print(treeCount)
