import sys
sys.path.append("..")
import tools, time
import mcpi.vec3 as vec3

if __name__ == '__main__':
    V3 = vec3.Vec3
    mc = tools.start(0)

    setb = mc.setBlock
    setbs = mc.setBlocks


    def heart(x, y, z):
        setb(x, y, z, 42)
        setb(x + 1, y, z, 42)
        setb(x - 1, y, z, 42)
        setb(x, y, z + 1, 42)
        setb(x, y, z - 1, 42)
        setb(x + 2, y, z, 41)
        setb(x - 2, y, z, 41)
        setb(x + 1, y, z + 1, 41)
        setb(x - 1, y, z + 1, 41)
        setb(x + 1, y, z - 1, 41)
        setb(x - 1, y, z - 1, 41)
        setb(x, y, z - 2, 41)
        setb(x, y, z + 2, 41)
        setb(x + 1, y, z + 2, 41)
        setb(x, y, z + 3, 42)
        setb(x + 1, y, z + 2, 42)
        setb(x - 1, y, z + 2, 42)
        # floor
        setb(x, y + 1, z + 4, 41)
        setb(x + 1, y + 2, z + 6, 42)
        setb(x + 3, y + 3, z + 6, 41)
        setb(x + 5, y + 4, z + 5, 42)
        setb(x + 7, y + 4, z + 3, 41)
        setb(x + 7, y + 5, z, 42)
        # block.WATER.id=8
        setb(x + 7, y + 6, z, 8)
        setb(x + 7, y + 6, z - 2, 41)
        setb(x + 5, y + 6, z - 4, 42)
        setb(x + 3, y + 7, z - 6, 41)
        setb(x + 1, y + 7, z - 7, 42)
        setb(x, y + 8, z - 8, 41)
        setb(x, y + 7, z - 6, 42)
        # block.LAVA.id=10
        setb(x, y + 8, z - 6, 10)
        setb(x - 1, y + 8, z - 7, 42)
        setb(x - 3, y + 8, z - 5, 41)
        setb(x - 5, y + 8, z - 3, 42)
        setb(x - 7, y + 9, z, 41)
        setb(x - 7, y + 10, z, 8)
        setb(x - 7, y + 10, z + 2, 42)
        setb(x - 5, y + 10, z + 4, 41)
        setb(x - 3, y + 11, z + 5, 42)


    start = map(int, input('the starting position:').split())
    pId = mc.getPlayerEntityId(map(mc.entity.getName, mc.getPlayerEntityIds()))
    mc.entity.setTilePos(pId, start)
    start = mc.entity.getTilePos(pId)
    x = start.x
    y = start.y
    z = start.z
    setchance = int(input('this task will be set for how many times:'))

    print("...")
    heart(x, y, z)
    i = 0
    while i < setchance:
        while True:
            if mc.entity.getTilePos(pId).y > y + 10:
                y += 11
                heart(x, y, z)
                break
            time.sleep(0.1)
        i += 1
    k = 0

    """while k>=0:
        setbs(x+8,y,z+8,x-8,y+k,z-8,0)
        time.sleep(3)
    k+=1"""
