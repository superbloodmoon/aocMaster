input = open('data.txt').read().splitlines()

validCount = 0

for i in input:
  key, letter, password = str(i).split()
  letter = letter[0]
  start, end = map(int, key.split("-"))

  if (password[start-1] == letter and password[end-1] != letter) or (password[start-1] != letter and password[end-1] == letter):
    validCount += 1

print(validCount)
  
