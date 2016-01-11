import string
import os
import csv

alphabet_dict = dict(zip(string.letters, [ord(c)%32 for c in string.letters] ))
tri_dict = dict()
for i in range(1, 100):
  tri_num = (i*(i+1))/2
  if tri_num > 364:
    break
  else:
    tri_dict[tri_num] = i

f = open(os.path.expanduser("~/Documents/Development/Python/Project/Euler/input/42.txt"), "r")

words = []

while True:
    line = f.readline()
    if not line: break
    for parsed_word in csv.reader([line]):
      words = parsed_word

answer = set()

for word in words:
  alphabet_sum = 0
  for x in word:
    alphabet_sum += alphabet_dict[x]
  
  if alphabet_sum in tri_dict:
    answer.add(word)


print answer
print len(answer)
