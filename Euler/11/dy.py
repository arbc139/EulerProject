import os

f = open(os.path.expanduser("~/Documents/Development/Python/Project/Euler/input/11.txt"), "r")

M = []
size = 20

while True: 
    line = f.readline()
    if not line: break

    M.append([int(n) for n in line.split()])

def MOperation(M, i, j, direction):
    if outCase(i, j, direction)

    result = M[i][j]


def outCase(i, j, direction):
    if direction == "left" and j<=2:
        return False
    elif direction == "right" and j>=size-3:
        return False
    elif direction == "up" and i<=2:
        return False
    elif direction == "down" and i>=size-3:
        return False
    elif direction == "leftUp" and (j<=2 or i<=2):
        return False
    elif direction == "rightUp" and (j>=size-3 or i<=2):
        return False
    elif direction == "leftDown" and (j<=2 or i>=size-3):
        return False
    elif direction == "rightDown" and (j>=size-3 or i>=size-3):
        return False
    else:   return True