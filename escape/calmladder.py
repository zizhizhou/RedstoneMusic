"""
Author: HarryTerpee
Theme: Calm ladder
"""
from .interface import *
import random


class CalmLadder(Level):
    HEIGHT = 12

    @staticmethod
    def exitWin(entrance: Window):
        entrance.height = CalmLadder.HEIGHT + 7
        if entrance.direction == Dir.N:
            entrance.direction = Dir.E
            entrance.middle.x += entrance.width // 2 + 3
            entrance.middle.y += CalmLadder.HEIGHT
            entrance.middle.z -= entrance.width // 2 + 2
        elif entrance.direction == Dir.E:
            entrance.direction = Dir.N
            entrance.middle.x += entrance.width // 2 + 2
            entrance.middle.y += CalmLadder.HEIGHT
            entrance.middle.z -= entrance.width // 2 + 3
        elif entrance.direction == Dir.S:
            entrance.direction = Dir.W
            entrance.middle.x -= entrance.width // 2 + 3
            entrance.middle.y += CalmLadder.HEIGHT
            entrance.middle.z += entrance.width // 2 + 2
        elif entrance.direction == Dir.W:
            entrance.direction = Dir.S
            entrance.middle.x -= entrance.width // 2 + 2
            entrance.middle.y += CalmLadder.HEIGHT
            entrance.middle.z += entrance.width // 2 + 3
        return entrance

    def setblock(self, x, y, z):
        self.mc.setBlock(x, y, z, 45)
        self.mc.setBlock(x + 1, y, z, 65, 5)
        self.mc.setBlock(x - 1, y, z, 65, 4)
        self.mc.setBlock(x, y, z + 1, 65, 3)
        self.mc.setBlock(x, y, z - 1, 65, 2)

    def _construct(self):
        direc = self.entWin.direction
        width = self.entWin.width
        halfwidth = width // 2
        height = CalmLadder.HEIGHT
        x, y, z = self.entWin.middle
        if direc == Dir.N:
            self.mc.setBlocks(x - halfwidth - 2, y - 1, z, x + halfwidth + 2, y + height + 8, z - width - 4, 45)
            self.mc.setBlocks(x - halfwidth - 1, y, z - 1, x + halfwidth + 1, y + height + 7, z - width - 3, 0)
            self.mc.setBlocks(x - halfwidth, y, z - 2, x + halfwidth, 0, z - width - 2, 0)
            self.mc.setBlocks(x + halfwidth + 2, y + height, z - 1, x + halfwidth + 2, y + height + 7, z - width - 3, 0)
            self.mc.setBlocks(x - halfwidth, y, z, x + halfwidth, y + 7, z, 0)
            for i in range(x - halfwidth, x + halfwidth, 2):
                for j in range(y, y + CalmLadder.HEIGHT, 3):
                    for k in range(z - width - 2, z - 2, 2):
                        m = random.randint(0, 3)
                        self.setblock(i + m, j + m, k + m)
        elif direc == Dir.S:
            self.mc.setBlocks(x - halfwidth - 2, y - 1, z, x + halfwidth + 2, y + height + 8, z + width + 4, 45)
            self.mc.setBlocks(x - halfwidth - 1, y, z + 1, x + halfwidth + 1, y + height + 7, z + width + 3, 0)
            self.mc.setBlocks(x - halfwidth, y, z + 2, x + halfwidth, 0, z + width + 2, 0)
            self.mc.setBlocks(x - halfwidth - 2, y + height, z + 1, x - halfwidth - 2, y + height + 7, z + width + 3, 0)
            self.mc.setBlocks(x - halfwidth, y, z, x + halfwidth, y + 7, z, 0)
            for i in range(x - halfwidth, x + halfwidth, 2):
                for j in range(y, y + CalmLadder.HEIGHT, 3):
                    for k in range(z + 2, z + width + 2, 2):
                        m = random.randint(0, 3)
                        self.setblock(i + m, j + m, k + m)
        elif direc == Dir.E:
            self.mc.setBlocks(x, y - 1, z - halfwidth - 2, x + width + 4, y + height + 8, z + halfwidth + 2, 45)
            self.mc.setBlocks(x + 1, y, z - halfwidth - 1, x + width + 3, y + height + 7, z + halfwidth + 1, 0)
            self.mc.setBlocks(x + 2, y, z - halfwidth, x + width + 2, 0, z + halfwidth, 0)
            self.mc.setBlocks(x + 1, y + height, z - halfwidth - 2, x + width + 3, y + height + 7, z - halfwidth - 2, 0)
            self.mc.setBlocks(x, y, z - halfwidth, x, y + 7, z + halfwidth, 0)
            for i in range(x + 2, x + width + 2, 3):
                for j in range(y, y + CalmLadder.HEIGHT, 3):
                    for k in range(z - halfwidth, z + halfwidth, 3):
                        m = random.randint(0, 3)
                        self.setblock(i + m, j + m, k + m)
        elif direc == Dir.W:
            self.mc.setBlocks(x, y - 1, z - halfwidth - 2, x - width - 4, y + height + 8, z + halfwidth + 2, 45)
            self.mc.setBlocks(x - 1, y, z - halfwidth - 1, x - width - 3, y + height + 7, z + halfwidth + 1, 0)
            self.mc.setBlocks(x - 2, y, z - halfwidth, x - width - 2, 0, z + halfwidth, 0)
            self.mc.setBlocks(x - 1, y + height, z + halfwidth + 2, x - width - 3, y + height + 7, z + halfwidth + 2, 0)
            self.mc.setBlocks(x, y, z - halfwidth, x, y + 7, z + halfwidth, 0)
            for i in range(x - width - 2, x - 2, 3):
                for j in range(y, y + CalmLadder.HEIGHT, 3):
                    for k in range(z - halfwidth, z + halfwidth, 3):
                        m = random.randint(0, 3)
                        self.setblock(i + m, j + m, k + m)

    def _loop(self):
        """静态关卡"""
        pass

    def _cleanup(self):
        pass
