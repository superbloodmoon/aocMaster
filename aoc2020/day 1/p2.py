input = open('data.txt').read().splitlines()

current = 0
current2 = 0 

for line in input:
  current = int(line)
  
  for line in input:
    current2 = int(line)
    for line in input:
      if int(line) + current + current2 == 2020:
        print(int(line) * current * current2)
        exit()
