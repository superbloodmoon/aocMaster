input = open('data.txt').read().splitlines()

validCount = 0

for i in input:
  key, letter, password = str(i).split()
  letter = letter[0]
  start, end = map(int, key.split("-"))

  if password.count(letter) in range(start, end+1):
    validCount += 1

print(validCount)
