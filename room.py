import mcpi.vec3 as vec3
import mcpi.minecraft as mmc
import mcpi.block as block
import random
from enum import IntEnum
import tools

V3 = vec3.Vec3
REVERSED = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e', 'b': 't', 't': 'b'}


class Gate(IntEnum):
    SEP = 0  # Separated
    AIR = 1  # Connected
    ACA = 2  # Acacia
    BIR = 3  # Brich
    DAR = 4  # Acacia
    JUN = 5  # Jungle
    SPR = 6  # Spruce
    WOO = 7  # Wood

    @staticmethod
    def randConn():
        """Random gate except for separation"""
        return max(Gate.AIR, random.choice(list(Gate)))


class Room:
    """Represents a room in Minecraft world."""

    def __init__(self, bottom: V3, length: int, height: int,
                 blockid=block.STONE_BRICK.id, **adjacent_rooms: dict):
        """Adjacent rooms: {s, n, e, w, b, t}"""
        self.blockid = blockid
        self.height = height
        self.length = length
        self.bottom = bottom
        self.adjacent = adjacent_rooms  # Direction: Room
        self.gates = {}  # Room: Gate
        self.walls = {'s': True, 'n': True, 'e': True, 'w': True, 'b': True, 't': True}

    def __repr__(self):
        """Here dx, dy, dz means regularized \"absolute\" position"""
        return "<Room dx={}, dy={}, dz={}>".format(
            self.bottom.x // self.length,
            self.bottom.y // self.height,
            self.bottom.z // self.length)

    def is_viable(self, rhs) -> bool:
        """Are the two rooms connected or not?"""
        return rhs in self.adjacent.values() and self.gates.get(rhs) != Gate.SEP

    def link(self, rhs, direction: str, connection: Gate):
        """Link two rooms"""
        self.adjacent[direction] = rhs
        rhs.adjacent[REVERSED[direction]] = self
        self.gates[rhs] = rhs.gates[self] = connection
        return self

    def __door(self, mc: mmc.Minecraft, dir: str, type: Gate):
        DOORS = {Gate.ACA: block.DOOR_ACACIA,
                 Gate.BIR: block.DOOR_BIRCH,
                 Gate.DAR: block.DOOR_DARK_OAK,
                 Gate.JUN: block.DOOR_JUNGLE,
                 Gate.SPR: block.DOOR_SPRUCE,
                 Gate.WOO: block.DOOR_WOOD}
        if type == Gate.SEP:
            return
        if dir == 'b':
            pos = self.bottom
        else:
            pos = self.bottom.__getattribute__(dir)(self.height if dir == 't' else self.length // 2)
        if type == Gate.AIR or dir == 'n' or dir == 'w':
            mc.setBlock(pos.up(), block.AIR.id)
            mc.setBlock(pos.up(2), block.AIR.id)
        else:
            mc.setBlock(pos.up(), DOORS[type].id, 0)  # Lower part
            mc.setBlock(pos.up(2), DOORS[type].id, 8)  # Upper part

    def __decorate(self, mc: mmc.Minecraft):
        if random.random() < 0.5:
            mc.setBlock(self.bottom.up(), block.TORCH.id)
        elif random.random() < 0.2:
            mc.setBlock(self.bottom, block.GLOWSTONE_BLOCK.id)
        elif random.random() < 0.1:
            mc.setBlock(self.bottom.down(), block.OBSIDIAN.id)
            mc.setBlock(self.bottom, block.LAVA.id)

    def construct(self, mc: mmc.Minecraft):
        tools.makeCubeAbove(mc, self.bottom, self.length, self.blockid, **self.walls)
        self.__decorate(mc)
        for dir, room in self.adjacent.items():
            self.__door(mc, dir, self.gates[room])
        return self

    def posIn(self, pos: V3) -> bool:
        return (self.bottom.x - self.length // 2 <= pos.x <= self.bottom.x + self.length // 2
                and self.bottom.z - self.length // 2 <= pos.z <= self.bottom.z + self.length // 2
                and self.bottom.y <= pos.y <= self.bottom.y + self.height)
