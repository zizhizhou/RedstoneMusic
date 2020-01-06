"""
Author: HarryTerpee
Theme: Terrify lava
"""
from .interface import *
from time import sleep
import mcpi.entity as entity
import random


class TerrifyLava(Level):
    LENGTH = 30
    HEIGHT = 7

    @staticmethod
    def exitWin(entrance: Window):
        entrance.height = TerrifyLava.HEIGHT
        if entrance.direction == Dir.N:
            entrance.middle.z -= TerrifyLava.LENGTH
        elif entrance.direction == Dir.S:
            entrance.middle.z += TerrifyLava.LENGTH
        elif entrance.direction == Dir.E:
            entrance.middle.x += TerrifyLava.LENGTH
        elif entrance.direction == Dir.W:
            entrance.middle.x -= TerrifyLava.LENGTH
        entrance.width = 5
        return entrance

    def _construct(self):
        HEIGHT, LENGTH = TerrifyLava.HEIGHT, TerrifyLava.LENGTH
        x, y, z = self.entWin.middle
        direction = self.entWin.direction
        setbs = self.mc.setBlocks
        setb = self.mc.setBlock
        halfwidth = self.entWin.width // 2
        if direction == Dir.E:
            setbs(x, y - 2, z - halfwidth - 1, x + LENGTH, y - 1, z + halfwidth + 1, 57)  # floor
            setbs(x, y - 1, z - halfwidth - 1, x + LENGTH, y + HEIGHT, z - halfwidth - 1, 57)  # left wall
            setbs(x, y - 1, z + halfwidth + 1, x + LENGTH, y + HEIGHT, z + halfwidth + 1, 57)  # right wall
            setbs(x, y + HEIGHT, z - halfwidth - 1, x + LENGTH, y + HEIGHT, z + halfwidth + 1, 57)  # ceiling
            setbs(x, y + HEIGHT // 2, z - halfwidth - 1, x + LENGTH, y + HEIGHT // 2, z - halfwidth - 1,
                  138)  # leftBeacon
            setbs(x, y + HEIGHT // 2, z + halfwidth + 1, x + LENGTH, y + HEIGHT // 2, z + halfwidth + 1,
                  138)  # rightBeacon
            setbs(x + 3, y - 1, z - halfwidth, x + LENGTH - 3, y - 1, z + halfwidth, 10)  # lava
            for i in range(x + 3, x + LENGTH - 3, 3):  # step
                for j in range(z - halfwidth, z + halfwidth, 3):
                    m = random.randint(0, 3)
                    setbs(i + m, y - 1, j + m, i + m + 1, y - 1, j + m, 57)
            setbs(x, y - 3, z - halfwidth - 2, x + LENGTH, y - 3, z + halfwidth + 2, 49)  # floor obsidian
            setbs(x, y - 3, z - halfwidth - 2, x + LENGTH, y + HEIGHT + 1, z - halfwidth - 2, 49)  # left wall obsidian
            setbs(x, y - 3, z + halfwidth + 2, x + LENGTH, y + HEIGHT + 1, z + halfwidth + 2, 49)  # right wall obsidian
            setbs(x, y + HEIGHT + 1, z - halfwidth - 2, x + LENGTH, y + HEIGHT + 1, z + halfwidth + 2,
                  49)  # ceiling obsidian
        elif direction == Dir.W:
            setbs(x, y - 2, z - halfwidth - 1, x - LENGTH, y - 1, z + halfwidth + 1, 57)
            setbs(x, y - 1, z - halfwidth - 1, x - LENGTH, y + HEIGHT, z - halfwidth - 1, 57)
            setbs(x, y - 1, z + halfwidth + 1, x - LENGTH, y + HEIGHT, z + halfwidth + 1, 57)
            setbs(x, y + HEIGHT, z - halfwidth - 1, x - LENGTH, y + HEIGHT, z + halfwidth + 1, 57)
            setbs(x, y + HEIGHT // 2, z - halfwidth - 1, x - LENGTH, y + HEIGHT // 2, z - halfwidth - 1, 138)
            setbs(x, y + HEIGHT // 2, z + halfwidth + 1, x - LENGTH, y + HEIGHT // 2, z + halfwidth + 1, 138)
            setbs(x - 3, y - 1, z - halfwidth, x - LENGTH + 3, y - 1, z + halfwidth, 10)
            for i in range(x - 3, x - LENGTH + 3, -3):
                for j in range(z - halfwidth, z + halfwidth, 3):
                    m = random.randint(0, 3)
                    setbs(i - m, y - 1, j + m, i - m - 1, y - 1, j + m, 57)
            setbs(x, y - 3, z - halfwidth - 2, x - LENGTH, y - 3, z + halfwidth + 2, 49)
            setbs(x, y - 3, z - halfwidth - 2, x - LENGTH, y + HEIGHT + 1, z - halfwidth - 2, 49)
            setbs(x, y - 3, z + halfwidth + 2, x - LENGTH, y + HEIGHT + 1, z + halfwidth + 2, 49)
            setbs(x, y + HEIGHT + 1, z - halfwidth - 2, x - LENGTH, y + HEIGHT + 1, z + halfwidth + 2, 49)
        elif direction == Dir.S:
            setbs(x - halfwidth - 1, y - 2, z, x + halfwidth + 1, y - 1, z + LENGTH, 57)
            setbs(x - halfwidth - 1, y - 1, z, x - halfwidth - 1, y + HEIGHT, z + LENGTH, 57)
            setbs(x + halfwidth + 1, y - 1, z, x + halfwidth + 1, y + HEIGHT, z + LENGTH, 57)
            setbs(x - halfwidth - 1, y + HEIGHT, z, x + halfwidth + 1, y + HEIGHT, z + LENGTH, 57)
            setbs(x + halfwidth + 1, y + HEIGHT // 2, z, x + halfwidth + 1, y + HEIGHT // 2, z + LENGTH, 138)
            setbs(x - halfwidth - 1, y + HEIGHT // 2, z, x - halfwidth - 1, y + HEIGHT // 2, z + LENGTH, 138)
            setbs(x - halfwidth, y - 1, z + 3, x + halfwidth, y - 1, z + LENGTH - 3, 10)
            for i in range(z + 3, z + LENGTH - 3, 3):
                for j in range(x - halfwidth, x + halfwidth, 3):
                    m = random.randint(0, 3)
                    setbs(j + m, y - 1, i + m, j + m, y - 1, i + m + 1, 57)
            setbs(x - halfwidth - 2, y - 3, z, x + halfwidth + 2, y - 3, z + LENGTH, 49)
            setbs(x - halfwidth - 2, y - 3, z, x - halfwidth - 2, y + HEIGHT + 1, z + LENGTH, 49)
            setbs(x + halfwidth + 2, y - 3, z, x + halfwidth + 2, y + HEIGHT + 1, z + LENGTH, 49)
            setbs(x - halfwidth - 2, y + HEIGHT + 1, z, x + halfwidth + 2, y + HEIGHT + 1, z + LENGTH, 49)
        elif direction == Dir.N:
            setbs(x - halfwidth - 1, y - 2, z, x + halfwidth + 1, y - 1, z - LENGTH, 57)
            setbs(x - halfwidth - 1, y - 1, z, x - halfwidth - 1, y + HEIGHT, z - LENGTH, 57)
            setbs(x + halfwidth + 1, y - 1, z, x + halfwidth + 1, y + HEIGHT, z - LENGTH, 57)
            setbs(x - halfwidth - 1, y + HEIGHT, z, x + halfwidth + 1, y + HEIGHT, z - LENGTH, 57)
            setbs(x + halfwidth + 1, y + HEIGHT // 2, z, x + halfwidth + 1, y + HEIGHT // 2, z - LENGTH, 138)
            setbs(x - halfwidth - 1, y + HEIGHT // 2, z, x - halfwidth - 1, y + HEIGHT // 2, z - LENGTH, 138)
            setbs(x - halfwidth, y - 1, z - 3, x + halfwidth, y - 1, z - LENGTH + 3, 10)
            for i in range(z - 3, z - LENGTH + 3, -3):
                for j in range(x - halfwidth, x + halfwidth, 3):
                    m = random.randint(0, 3)
                    setbs(j + m, y - 1, i - m, j + m, y - 1, i - m - 1, 57)
            setbs(x - halfwidth - 2, y - 3, z, x + halfwidth + 2, y - 3, z - LENGTH, 49)
            setbs(x - halfwidth - 2, y - 3, z, x - halfwidth - 2, y + HEIGHT + 1, z - LENGTH, 49)
            setbs(x + halfwidth + 2, y - 3, z, x + halfwidth + 2, y + HEIGHT + 1, z - LENGTH, 49)
            setbs(x - halfwidth - 2, y + HEIGHT + 1, z, x + halfwidth + 2, y + HEIGHT + 1, z - LENGTH, 49)

    def _loop(self):
        for p in self.players:
            ppos = self.mc.entity.getTilePos(p)  # player position
            self.mc.spawnEntity(ppos.x, self.entWin.middle.y + self.HEIGHT, ppos.z, entity.PRIMED_TNT.id)
        sleep(1)

    def _cleanup(self):
        pass
