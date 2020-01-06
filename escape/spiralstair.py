import sys
sys.path.append("..")
import mcpi.minecraft as mmc
import tools, time
import mcpi.block as block
import mcpi.entity as entity
import mcpi.vec3 as vec3
from escape.interface import *

if __name__ == '__main__':
    V3 = vec3.Vec3
    mc = tools.start(0)


class SpiralStair(Level):
    @staticmethod
    def exitWin(entrance: Window):
        entrance.middle.y += 10
        return entrance

    def _construct(self):
        setb = self.mc.setBlock
        setbs = self.mc.setBlocks
        x, y, z = self.entWin.middle
        setbs(x + 2, y - 1, z - 8, x + 4, y + 10, z + 8, 0)
        setbs(x - 2, y - 1, z - 8, x - 4, y + 10, z + 8, 0)
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
        setb(x, y + 11, z + 2, 42)
        setb(x + 1, y + 11, z + 2, 42)
        setb(x - 1, y + 11, z + 2, 42)
        setb(x, y + 11, z + 3, 42)
        setb(x, y + 11, z + 1, 42)
        setb(x + 2, y + 11, z + 2, 41)
        setb(x - 2, y + 11, z + 2, 41)
        setb(x + 1, y + 11, z + 3, 41)
        setb(x - 1, y + 11, z + 3, 41)
        setb(x + 1, y + 11, z + 1, 41)
        setb(x - 1, y + 11, z + 1, 41)
        setb(x, y + 11, z, 41)
        setb(x, y + 11, z + 4, 41)

    def _loop(self):
        """静态关卡"""
        pass

    def _cleanup(self):
        pass
