import sys, random

sys.path.append("..")
import tools
mc = tools.start(0)
WIDTH = 11
HALFWIDTH = 3
LENGTH = 101
direction = input('the direction is: ')
setbs = mc.setBlocks
setb = mc.setBlock
pId = mc.getPlayerEntityId(map(mc.entity.getName, mc.getPlayerEntityIds()))
start = mc.entity.getTilePos(pId)
x = start.x
y = start.y
z = start.z
color = random.randint(1, 16)
if direction == 'e':
    setbs(x + 1, y - 1, z - HALFWIDTH, x + LENGTH, y - 1, z + HALFWIDTH, 160, color)
    setbs(x + 1, y - 1, z - WIDTH // 2 - 1, x + LENGTH, y + 7, z - WIDTH // 2 - 1, 95, color)
    setbs(x + 1, y - 1, z + WIDTH // 2 + 1, x + LENGTH, y + 7, z + WIDTH // 2 + 1, 95, color)
    setbs(x + 1, y + 7, z + WIDTH // 2 + 1, x + LENGTH, y + 7, z - WIDTH // 2 - 1, 95, color)
    setbs(x + 1, y - 2, z - HALFWIDTH, x + LENGTH, 0, z + HALFWIDTH, 0)
    setbs(x + 1, y - 1, z - HALFWIDTH, x + LENGTH, 0, z - WIDTH // 2, 0)
    setbs(x + 1, y - 1, z + HALFWIDTH, x + LENGTH, 0, z + WIDTH // 2, 0)
    for i in range(x + 1, x + LENGTH - 2, 2):
        for j in range(z - HALFWIDTH, z + HALFWIDTH, 2):
            m = random.randint(0, 2)
            setbs(i + m, y - 1, j + m, i + m + 1, y - 1, j + m, 0)
elif direction == 'w':
    setbs(x - 1, y - 1, z - HALFWIDTH, x - LENGTH, y - 1, z + HALFWIDTH, 160, color)
    setbs(x - 1, y - 1, z - WIDTH // 2 - 1, x - LENGTH, y + 7, z - WIDTH // 2 - 1, 95, color)
    setbs(x - 1, y - 1, z + WIDTH // 2 + 1, x - LENGTH, y + 7, z + WIDTH // 2 + 1, 95, color)
    setbs(x - 1, y + 7, z + WIDTH // 2 + 1, x - LENGTH, y + 7, z - WIDTH // 2 - 1, 95, color)
    setbs(x - 1, y - 2, z - HALFWIDTH, x - LENGTH, 0, z + HALFWIDTH, 0)
    setbs(x - 1, y - 1, z - HALFWIDTH, x - LENGTH, 0, z - WIDTH // 2, 0)
    setbs(x - 1, y - 1, z + HALFWIDTH, x - LENGTH, 0, z + WIDTH // 2, 0)
    for i in range(x - LENGTH, x - 3, 2):
        for j in range(z - HALFWIDTH, z + HALFWIDTH, 2):
            m = random.randint(0, 2)
            setbs(i + m, y - 1, j + m, i + m + 1, y - 1, j + m, 0)
elif direction == 'n':
    setbs(x - HALFWIDTH, y - 1, z - 1, x + HALFWIDTH, y - 1, z - LENGTH, 160, color)
    setbs(x - WIDTH // 2 - 1, y - 1, z - 1, x - WIDTH // 2 - 1, y + 7, z - LENGTH, 95, color)
    setbs(x + WIDTH // 2 + 1, y - 1, z - 1, x + WIDTH // 2 + 1, y + 7, z - LENGTH, 95, color)
    setbs(x + WIDTH // 2 + 1, y + 7, z - 1, x - WIDTH // 2 - 1, y + 7, z - LENGTH, 95, color)
    setbs(x - HALFWIDTH, y - 2, z - 1, x + HALFWIDTH, 0, z - LENGTH, 0)
    setbs(x - HALFWIDTH, y - 1, z - 1, x - WIDTH // 2, 0, z - LENGTH, 0)
    setbs(x + HALFWIDTH, y - 1, z - 1, x + WIDTH // 2, 0, z - LENGTH, 0)
    for i in range(z - LENGTH, z - 3, 2):
        for j in range(x - HALFWIDTH, x + HALFWIDTH, 2):
            m = random.randint(0, 2)
            setbs(j + m, y - 1, i + m, j + m, y - 1, i + m + 1, 0)
elif direction == 's':
    setbs(x - HALFWIDTH, y - 1, z + 1, x + HALFWIDTH, y - 1, z + LENGTH, 160, color)
    setbs(x - WIDTH // 2 - 1, y - 1, z + 1, x - WIDTH // 2 - 1, y + 7, z + LENGTH, 95, color)
    setbs(x + WIDTH // 2 + 1, y - 1, z + 1, x + WIDTH // 2 + 1, y + 7, z + LENGTH, 95, color)
    setbs(x + WIDTH // 2 + 1, y + 7, z + 1, x - WIDTH // 2 - 1, y + 7, z + LENGTH, 95, color)
    setbs(x - HALFWIDTH, y - 2, z + 1, x + HALFWIDTH, 0, z + LENGTH, 0)
    setbs(x - HALFWIDTH, y - 1, z + 1, x - WIDTH // 2, 0, z + LENGTH, 0)
    setbs(x + HALFWIDTH, y - 1, z + 1, x + WIDTH // 2, 0, z + LENGTH, 0)
    for i in range(z + 1, z + LENGTH - 2, 2):
        for j in range(x - HALFWIDTH, x + HALFWIDTH, 2):
            m = random.randint(0, 2)
            setbs(j + m, y - 1, i + m, j + m, y - 1, i + m + 1, 0)
