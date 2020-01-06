# import sys
# sys.path.append("..")
from typing import Type

import mcpi.minecraft as mmc
import mcpi.vec3 as vec3
from mcpi.vec3 import Vec3
from escape.interface import Dir

V3: Type[Vec3] = vec3.Vec3


def start(port=-1) -> mmc.Minecraft:
    """Return Minecraft connection \"mc\""""
    print('''######################################
#                                    #
#    Raspy Control Initialization    #
#                                    #
######################################
''')
    if port == -1:
        while True:
            try:
                port = int(input("Please specify the natapp port if given; input 0 to connect to local host: "))
            except ValueError:
                print("That wasn't a valid integer.")
            else:
                break
    if port:
        mc = mmc.Minecraft.create("server.natappfree.cc", port)
    else:
        mc = mmc.Minecraft.create()
    print('Minecraft connection "mc" established!')
    return mc


def getpid(mc: mmc.Minecraft) -> int:
    """Return the first player's id"""
    return mc.getPlayerEntityIds()[0]


def makeCubeCenter(mc, center, length, blockid,
                   s=True, n=True, e=True, w=True, t=True, b=True):
    """Construct a room. s, n, ..., b for corresponding walls"""
    r = length // 2
    se = V3(r, -r, r) + center
    ne = V3(r, r, -r) + center
    sw = V3(-r, r, r) + center
    nw = V3(-r, -r, -r) + center
    if s: mc.setBlocks(sw, se, blockid)
    if n: mc.setBlocks(nw, ne, blockid)
    if e: mc.setBlocks(se, ne, blockid)
    if w: mc.setBlocks(sw, nw, blockid)
    if b: mc.setBlocks(nw, se, blockid)
    if t: mc.setBlocks(ne, sw, blockid)


def makeCubeAbove(mc, bottom, length, blockid,
                  s=True, n=True, e=True, w=True, t=True, b=True):
    """Construct a room above. s, n, ..., b for corresponding walls"""
    makeCubeCenter(mc, bottom + V3(0, length // 2, 0),
                   length, blockid, s, n, e, w, t, b)


def makeCubeVertex(mc, vertex, length, blockid,
                   s=True, n=True, e=True, w=True, t=True, b=True):
    """Construct a room with vertex at NW bottom. s, n, ..., b for corresponding walls"""
    makeCubeCenter(mc, vertex + V3(length // 2, length // 2, length // 2),
                   length, blockid, s, n, e, w, t, b)


def east_shift(original: V3, shift: V3, direction: Dir):
    """Assume east is the direction and specify the coordinate shifts"""
    if direction == Dir.E:
        return original + shift
    elif direction == Dir.W:
        return V3(original.x - shift.x, original.y + shift.y, original.z - shift.z)
    elif direction == Dir.N:
        return V3(original.x + shift.z, original.y + shift.y, original.z - shift.x)
    elif direction == Dir.S:
        return V3(original.x - shift.z, original.y + shift.y, original.z + shift.x)
    elif direction == Dir.T:
        return V3(original.x + shift.y, original.y + shift.x, original.z + shift.z)
    elif direction == Dir.B:
        return V3(original.x - shift.y, original.y - shift.x, original.z + shift.z)
