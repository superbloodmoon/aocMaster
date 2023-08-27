#2020 day 3

input = open('input.txt').read().splitlines()

treeProduct = 1

slopes = [[1,1], [3,1], [5,1], [7, 1], [1,2]]

for slope in slopes:
  xPosition, yPosition = 0, 0
  treeCount = 0
  print(slope[0], slope[1])
  
  while yPosition < len(input):
    line = input[yPosition]
    
    if list(line)[xPosition % len(line)] == "#": treeCount += 1
  
    xPosition += slope[0]
    yPosition += slope[1]

  treeProduct *= treeCount

print(treeProduct)
