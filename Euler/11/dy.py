import os

f = open(os.path.expanduser("~/Documents/Development/Python/Project/Euler/input/11.txt"), "r")

M = []
size = 20

while True: 
    line = f.readline()
    if not line: break

    M.append([int(n) for n in line.split()])


answer = set()

print M

def find_horizontal():
  for row in M:
    for idx in range(0, 17):
      partial_row = row[idx:idx+4]
      answer.add(reduce(lambda x, y: x*y, partial_row))

def find_vertical():
  for c_idx in range(0, 20):
    for r_idx in range(0, 17):
      partial_sum = M[r_idx][c_idx] * M[r_idx+1][c_idx] * M[r_idx+2][c_idx] * M[r_idx+3][c_idx]
      answer.add(partial_sum)

def find_upCross():
  for r_idx in range(3, 20):
    for c_idx in range(0, 17):
      partial_sum = M[r_idx][c_idx] * M[r_idx-1][c_idx+1] * M[r_idx-2][c_idx+2] * M[r_idx-3][c_idx+3]
      answer.add(partial_sum)


def find_downCross():
  for r_idx in range(0, 17):
    for c_idx in range(0, 17):
      partial_sum = M[r_idx][c_idx] * M[r_idx+1][c_idx+1] * M[r_idx+2][c_idx+2] * M[r_idx+3][c_idx+3]
      answer.add(partial_sum)

find_horizontal()
find_vertical()
find_upCross()
find_downCross()

print max(answer)