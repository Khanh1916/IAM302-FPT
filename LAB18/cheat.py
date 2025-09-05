import os

# Dump memory
os.system("del mine.dmp")
os.system("procdump -ma minesam.exe mine")

# Find gameboard
mark = '\x28\x00\x00\x00\x10\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x10\x10\x10\x10'
nread = 20
boardfound = 0
gameboard = []

with open("mine.dmp", "rb") as f:
    line = f.read(20)
    while boardfound == 0:
        c = f.read(1)
        if c == b"":  # Python 3: bytes so prefix with b
            print("File ended, but gameboard not found!")
            exit()
        line = line[1:] + c
        nread += 1

        if nread % 0x100000 == 0:
            print("Looking at byte", hex(nread), nread)

        if line == mark:
            print("Gameboard found at", hex(nread))
            boardfound = 1

    for i in range(4):
        gameboard.append(b'\x10')

    for i in range(500):
        gameboard.append(f.read(1))

# Print Gameboard
l = len(gameboard)
m = 32  # items per line

for i in range(0, l - m, m):
    line = ""
    for j in range(m):
        g = gameboard[i + j]
        if g == b'\x10':
            c = "-"
        elif g == b'\x0f':
            c = " "
        elif g == b'\x8f':
            c = "*"
        elif g == b'\x00':
            c = " "
        else:
            c = chr(ord(g)) if isinstance(g, str) else chr(g[0] - 16)
        line += c
    print(line)
