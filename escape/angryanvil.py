"""
Author: HarryTerpee
Theme: Angry Anvil
"""
from escape.interface import *
from mcpi import block
import random
from time import sleep


class AngryAnvil(Level):
    LENGTH = 50
    NUMBER = LENGTH // 4
    FLASH_PERIOD = 0.2
    FLASH_TIMES = 3
    ANV = block.ANVIL.id
    SHC = block.STAINED_HARDENED_CLAY.id
    SND = block.SANDSTONE.id

    @staticmethod
    def exitWin(entrance: Window):
        dir = entrance.direction
        if dir == Dir.N:
            entrance.middle.z -= AngryAnvil.LENGTH
        elif dir == Dir.S:
            entrance.middle.z += AngryAnvil.LENGTH
        elif dir == Dir.E:
            entrance.middle.x += AngryAnvil.LENGTH
        elif dir == Dir.W:
            entrance.middle.x -= AngryAnvil.LENGTH
        entrance.height = 7
        entrance.width = 3
        return entrance

    def _construct(self):
        LENGTH = AngryAnvil.LENGTH
        setbs = self.mc.setBlocks
        x, y, z = self.entWin.middle
        width = self.entWin.width
        print(width)
        if self.entWin.direction == Dir.N:
            setbs(x - 1, y - 1, z, x + 1, y - 1, z - LENGTH, AngryAnvil.SHC, 4)
            setbs(x - 2, y - 1, z, x - 2, y + 7, z - LENGTH, AngryAnvil.SND, 1)
            setbs(x + 2, y - 1, z, x + 2, y + 7, z - LENGTH, AngryAnvil.SND, 1)
            setbs(x - width // 2 - 1, y, z, x - 2, y + 7, z, AngryAnvil.SND, 1)
            setbs(x + width // 2 + 1, y, z, x + 2, y + 7, z, AngryAnvil.SND, 1)
        elif self.entWin.direction == Dir.S:
            setbs(x - 1, y - 1, z, x + 1, y - 1, z + LENGTH, AngryAnvil.SHC, 4)
            setbs(x - 2, y - 1, z, x - 2, y + 7, z + LENGTH, AngryAnvil.SND, 1)
            setbs(x + 2, y - 1, z, x + 2, y + 7, z + LENGTH, AngryAnvil.SND, 1)
            setbs(x - width // 2 - 1, y, z, x - 2, y + 7, z, AngryAnvil.SND, 1)
            setbs(x + width // 2 + 1, y, z, x + 2, y + 7, z, AngryAnvil.SND, 1)
        elif self.entWin.direction == Dir.E:
            setbs(x, y - 1, z - 1, x + LENGTH, y - 1, z + 1, AngryAnvil.SHC, 4)
            setbs(x, y - 1, z - 2, x + LENGTH, y + 7, z - 2, AngryAnvil.SND, 1)
            setbs(x, y - 1, z + 2, x + LENGTH, y + 7, z + 2, AngryAnvil.SND, 1)
            setbs(x, y, z - width // 2 - 1, x, y + 7, z - 2, AngryAnvil.SND, 1)
            setbs(x, y, z + width // 2 + 1, x, y + 7, z + 2, AngryAnvil.SND, 1)
        elif self.entWin.direction == Dir.W:
            setbs(x, y - 1, z - 1, x - LENGTH, y - 1, z + 1, AngryAnvil.SHC, 4)
            setbs(x, y - 1, z - 2, x - LENGTH, y + 7, z - 2, AngryAnvil.SND, 1)
            setbs(x, y - 1, z + 2, x - LENGTH, y + 7, z + 2, AngryAnvil.SND, 1)
            setbs(x, y, z - width // 2 - 1, x, y + 7, z - 2, AngryAnvil.SND, 1)
            setbs(x, y, z + width // 2 + 1, x, y + 7, z + 2, AngryAnvil.SND, 1)

    def area(self) -> List[Tuple[int, int, int]]:
        """选定并返回闪烁地点"""
        x, y, z = self.entWin.middle
        direction = self.entWin.direction
        pos = []
        for _ in range(0, AngryAnvil.NUMBER):
            if direction == Dir.S:
                i = random.randint(x - 1, x + 1)
                j = random.randint(z, z + AngryAnvil.LENGTH)
                pos.append((i, y, j))
            elif direction == Dir.N:
                i = random.randint(x - 1, x + 1)
                j = random.randint(z - AngryAnvil.LENGTH, z)
                pos.append((i, y, j))
            elif direction == Dir.W:
                i = random.randint(z - 1, z + 1)
                j = random.randint(x - AngryAnvil.LENGTH, x)
                pos.append((j, y, i))
            elif direction == Dir.E:
                i = random.randint(z - 1, z + 1)
                j = random.randint(x, x + AngryAnvil.LENGTH)
                pos.append((j, y, i))
        return pos

    def _loop(self):
        """闪烁，落铁砧"""
        if not self.players:
            return
        setb = self.mc.setBlock
        pos = self.area()
        i = 0
        while i < AngryAnvil.FLASH_TIMES:
            for m in range(0, AngryAnvil.NUMBER):
                setb(pos[m][0], pos[m][1] - 1, pos[m][2], AngryAnvil.SHC, 4)  # yellow clay
            sleep(AngryAnvil.FLASH_PERIOD)
            for m in range(0, AngryAnvil.NUMBER):
                setb(pos[m][0], pos[m][1] - 1, pos[m][2], AngryAnvil.SHC, 14)  # red clay
            sleep(AngryAnvil.FLASH_PERIOD)
            for m in range(0, AngryAnvil.NUMBER):
                if i == 1: setb(pos[m][0], pos[m][1] + 7, pos[m][2], AngryAnvil.ANV)  # anvil
            i += 1

    def _cleanup(self):
        pass
