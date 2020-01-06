import sys
sys.path.append("..")
import mcpi.minecraft as mmc
import tools, time
import mcpi.block as block
import mcpi.entity as entity
import mcpi.vec3 as vec3
from escape.tnt import tntfollow

if __name__ == '__main__':
    V3 = vec3.Vec3
    mc = tools.start(0)
    import random, math


    setb = mc.setBlock
    setbs = mc.setBlocks
    halfwidth=5
    LENGTH=20
    HEIGHT=7


    def east(x, y, z):
        setbs(x, y - 2, z - halfwidth, x + LENGTH, y - 1, z + halfwidth, 57)  # floor
        setbs(x, y - 1, z - halfwidth, x + LENGTH, y + HEIGHT, z - halfwidth, 57)  # leftwall
        setbs(x, y - 1, z + halfwidth, x + LENGTH, y + HEIGHT, z + halfwidth, 57)  # rightwall
        setbs(x, y + HEIGHT, z - halfwidth, x + LENGTH, y + HEIGHT, z + halfwidth, 57) #ceiling
        setbs(x, y - 3, z - halfwidth, x + LENGTH, y - 3, z + halfwidth, 49)  # floor obsidian
        setbs(x, y - 3, z - halfwidth - 1, x + LENGTH, y + HEIGHT + 1, z - halfwidth - 1, 49)  # leftwall obsidian
        setbs(x, y - 3, z + halfwidth + 1, x + LENGTH, y + HEIGHT + 1, z + halfwidth + 1, 49)  # rightwall obsidian
        setbs(x, y + HEIGHT + 1, z - halfwidth - 1, x + LENGTH, y + HEIGHT + 1, z + halfwidth + 1, 49) #ceiling obsidian
        setbs(x, y + HEIGHT//2, z - halfwidth, x + LENGTH, y + HEIGHT//2, z - halfwidth, 138)  # leftBeacon
        setbs(x, y + HEIGHT//2, z + halfwidth, x + LENGTH, y + HEIGHT//2, z + halfwidth, 138)  # rightBeacon
        setbs(x + 3, y - 1, z - 4, x + LENGTH - 3, y - 1, z + 4, 10)  # lava
        for i in range(x + 3, x + LENGTH - 3, 3):  # step
            for j in range(z - 4, z + 4, 3):
                m = random.randint(0, 3)
                setbs(i + m, y - 1, j + m, i + m + 1, y - 1, j + m, 57)


    def west(x, y, z):
        setbs(x, y - 2, z - halfwidth, x - LENGTH, y - 1, z + halfwidth, 57)
        setbs(x, y - 1, z - halfwidth, x - LENGTH, y + HEIGHT, z - halfwidth, 57)
        setbs(x, y - 1, z + halfwidth, x - LENGTH, y + HEIGHT, z + halfwidth, 57)
        setbs(x, y + HEIGHT, z - halfwidth, x - LENGTH, y + HEIGHT, z + halfwidth, 57)
        setbs(x, y - 3, z - halfwidth - 1, x - LENGTH, y - 3, z + halfwidth + 1, 49)
        setbs(x, y - 3, z - halfwidth - 1, x - LENGTH, y + HEIGHT + 1, z - halfwidth - 1, 49)
        setbs(x, y - 3, z + halfwidth + 1, x - LENGTH, y + HEIGHT + 1, z + halfwidth + 1, 49)
        setbs(x, y + HEIGHT, z - halfwidth - 1, x - LENGTH, y + HEIGHT + 1, z + halfwidth + 1, 49)
        setbs(x, y + HEIGHT//2, z - halfwidth, x - LENGTH, y + HEIGHT//2, z - halfwidth, 138)
        setbs(x, y + HEIGHT//2, z + halfwidth, x - LENGTH, y + HEIGHT//2, z + halfwidth, 138)
        setbs(x - 3, y - 1, z - 4, x - LENGTH + 3, y - 1, z + 4, 10)
        for i in range(x - 3, x - LENGTH + 3, -3):
            for j in range(z - 4, z + 4, 3):
                m = random.randint(0, 3)
                setbs(i - m, y - 1, j + m, i - m - 1, y - 1, j + m, 57)


    def south(x, y, z):
        setbs(x - halfwidth, y - 2, z, x + halfwidth, y - 1, z + LENGTH, 57)
        setbs(x - halfwidth, y - 1, z, x - halfwidth, y + HEIGHT, z + LENGTH, 57)
        setbs(x + halfwidth, y - 1, z, x + halfwidth, y + HEIGHT, z + LENGTH, 57)
        setbs(x - halfwidth, y + HEIGHT, z ,x + halfwidth, y + HEIGHT, z + LENGTH, 57)
        setbs(x - halfwidth - 1, y - 3, z, x + halfwidth + 1, y - 3, z + LENGTH, 49)
        setbs(x - halfwidth - 1, y - 3, z, x - halfwidth - 1, y + HEIGHT + 1, z + LENGTH, 49)
        setbs(x + halfwidth + 1, y - 3, z, x + halfwidth + 1, y + HEIGHT + 1, z + LENGTH, 49)
        setbs(x - halfwidth - 1, y + HEIGHT + 1, z ,x + halfwidth + 1, y + HEIGHT + 1, z + LENGTH, 49)
        setbs(x + halfwidth, y + HEIGHT//2, z, x + halfwidth, y + HEIGHT//2, z + LENGTH, 138)
        setbs(x - halfwidth, y + HEIGHT//2, z, x - halfwidth, y + HEIGHT//2, z + LENGTH, 138)
        setbs(x - 4, y - 1, z + 3, x + 4, y - 1, z + LENGTH - 3, 10)
        for i in range(z + 3, z + LENGTH - 3, 3):
            for j in range(x - 4, x + 4, 3):
                m = random.randint(0, 3)
                setbs(j + m, y - 1, i + m, j + m, y - 1, i + m + 1, 57)


    def north(x, y, z):
        setbs(x - halfwidth, y - 2, z, x + halfwidth, y - 1, z - LENGTH, 57)
        setbs(x - halfwidth, y - 1, z, x - halfwidth, y + HEIGHT, z - LENGTH, 57)
        setbs(x + halfwidth, y - 1, z, x + halfwidth, y + HEIGHT, z - LENGTH, 57)
        setbs(x - halfwidth, y + HEIGHT, z, x + halfwidth, y + HEIGHT, z - LENGTH, 57)
        setbs(x - halfwidth - 1, y - 3, z, x + halfwidth + 1, y - 3, z - LENGTH, 49)
        setbs(x - halfwidth - 1, y - 3, z, x - halfwidth - 1, y + HEIGHT + 1, z - LENGTH, 49)
        setbs(x + halfwidth + 1, y - 3, z, x + halfwidth + 1, y + HEIGHT + 1, z - LENGTH, 49)
        setbs(x - halfwidth - 1, y + HEIGHT + 1, z, x + halfwidth + 1, y + HEIGHT + 1, z - LENGTH, 49)
        setbs(x + halfwidth, y + HEIGHT//2, z, x + halfwidth, y + HEIGHT//2, z - LENGTH, 138)
        setbs(x - halfwidth, y + HEIGHT//2, z, x - halfwidth, y + HEIGHT//2, z - LENGTH, 138)
        setbs(x - 4, y - 1, z - 3, x + 4, y - 1, z - LENGTH + 3, 10)
        for i in range(z - 3, z - LENGTH + 3, -3):
            for j in range(x - 4, x + 4, 3):
                m = random.randint(0, 3)
                setbs(j + m, y - 1, i - m, j + m, y - 1, i - m - 1, 57)


    #start = map(int, input('the starting position:').split())
    direction = input('''the starting direction(east='e',north='n',south='s',west='w'):''')
    pId = mc.getPlayerEntityId(map(mc.entity.getName, mc.getPlayerEntityIds()))
    start = mc.entity.getTilePos(pId)
    #mc.entity.setTilePos(pId, start)
    x = start.x
    y = start.y
    z = start.z
    setchance = int(input('this task will be set for how many times:'))
    from multiprocessing import Process
    import os
    import escape.tnt

    print("Initializing TNT follow.")
    p = Process(target=tntfollow, args=(0, 20))
    if direction == 'e':
        east(x, y, z)
        p.start()
        i = 0
        while i < setchance:
            while True:
                if mc.entity.getTilePos(pId).x > x + 5:
                    x += 18
                    east(x, y, z)
                    break
                time.sleep(0.1)
            i += 1
    elif direction == 'n':
        north(x, y, z)
        p.start()
        i = 0
        while i < setchance:
            while True:
                if mc.entity.getTilePos(pId).z < z - 5:
                    z -= 18
                    north(x, y, z)
                    break
                time.sleep(0.1)
            i += 1
    elif direction == 's':
        south(x, y, z)
        p.start()
        i = 0
        while i < setchance:
            while True:
                if mc.entity.getTilePos(pId).z > z + 5:
                    z += 18
                    south(x, y, z)
                    break
                time.sleep(0.1)
            i += 1
    elif direction == 'w':
        west(x, y, z)
        p.start()
        i = 0
        while i < setchance:
            while True:
                if mc.entity.getTilePos(pId).x < x - 5:
                    x -= 18
                    west(x, y, z)
                    break
                time.sleep(0.1)
            i += 1
