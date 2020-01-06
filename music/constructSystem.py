# --------------------
# constructSystem.py
# Attach the configured redstone system in game
# --------------------

import sys
sys.path.append("..")

import mcpi.block as block
import mcpi.connection
import setSystem as ss

# rN: repeaterNum
# cRPL: columnRelativePlacingList

# --------------------
# xBoundary
# --------------------

def xBoundary(cRPL):
    """Define the horizontal boundary of glass cover"""
    return [cRPL[0] - 2, cRPL[-1] + 2]

# --------------------
# zBoundary
# --------------------

def zBoundary(minDelay, rN, processedList):
    """Define the vertical boundary of glass cover"""
    if processedList[-1][0] == 0:      # hitNum == 1
        num = 1
    else:
        num = int(processedList[-1][0] / minDelay) + 1
    length = 4 + (num - 1) * (2 + rN) + 4
    return [-1, -1 + length - 1]

# --------------------
# placeStone
# --------------------

def placeStone(loc, xBoundary, zBoundary, gameName):
    # place stone in the bottom
    gameName.setBlocks(
        loc.x + xBoundary[0], loc.y - 1, loc.z + zBoundary[0],
        loc.x + xBoundary[1], loc.y - 1, loc.z + zBoundary[1],
        block.STONE.id)

# --------------------
# placeGlass
# --------------------

def placeGlass(loc, xBoundary, zBoundary, gameName):
    # place in the front and in the back
    gameName.setBlocks(
        loc.x + xBoundary[0], loc.y, loc.z + zBoundary[0],
        loc.x + xBoundary[1], loc.y + 6, loc.z + zBoundary[0],
        block.GLASS.id)
    gameName.setBlocks(
        loc.x + xBoundary[0], loc.y, loc.z + zBoundary[1],
        loc.x + xBoundary[1], loc.y + 6, loc.z + zBoundary[1],
        block.GLASS.id)
    # place in the left and in the right
    gameName.setBlocks(
        loc.x + xBoundary[0], loc.y, loc.z + zBoundary[0],
        loc.x + xBoundary[0], loc.y + 6, loc.z + zBoundary[1],
        block.GLASS.id)
    gameName.setBlocks(
        loc.x + xBoundary[1], loc.y, loc.z + zBoundary[0],
        loc.x + xBoundary[1], loc.y + 6, loc.z + zBoundary[1],
        block.GLASS.id)
    # place the top cover
    gameName.setBlocks(
        loc.x + xBoundary[0], loc.y + 7, loc.z + zBoundary[0],
        loc.x + xBoundary[1], loc.y + 7, loc.z + zBoundary[1],
        block.GLASS.id)

# --------------------
# placeAir
# --------------------

def placeAir(loc, xBoundary, zBoundary, gameName):
    # place inside glass cover
        gameName.setBlocks(
        loc.x + xBoundary[0] + 1, loc.y + 0, loc.z + zBoundary[0] + 1,
        loc.x + xBoundary[1] - 1, loc.y + 6, loc.z + zBoundary[1] - 1,
        block.AIR.id)

# --------------------
# placeDoor
# --------------------

def placeDoor(loc, zBoundary, gameName):
    # place front door
    gameName.setBlock(loc.x, loc.y, loc.z + zBoundary[0], block.DOOR_BIRCH.id, 0)
    gameName.setBlock(loc.x, loc.y + 1, loc.z + zBoundary[0], block.DOOR_BIRCH.id, 8)

    # place back door
    gameName.setBlock(loc.x, loc.y, loc.z + zBoundary[1], block.DOOR_BIRCH.id, 0)
    gameName.setBlock(loc.x, loc.y + 1, loc.z + zBoundary[1], block.DOOR_BIRCH.id, 9)

# --------------------
# placeNoteBlock
# --------------------

def placeNoteBlock(loc, configWay, hitNum, minDelay, rN, cRPL, processedList, gameName):

    if configWay[0] == 1:
        for j in range(0, hitNum):
            for k in range(0, len(processedList[j][1])):      # the number of notes in noteProcessedList[j]
                gameName.setNoteBlock(loc.x + cRPL[k], loc.y, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), processedList[j][1][k])

        if configWay[1] == 1:      # harp/piano timbre
            for j in range(0, hitNum):
                for k in range(0, len(processedList[j][1])):
                    gameName.setBlock(loc.x + cRPL[k], loc.y - 1, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), block.GRASS.id)
        elif configWay[1] == 2:      # double bass timbre
            for j in range(0, hitNum):
                for k in range(0, len(processedList[j][1])):
                    gameName.setBlock(loc.x + cRPL[k], loc.y - 1, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), block.WOOD.id)
        elif configWay[1] == 3:      # glockenspiel timbre
            for j in range(0, hitNum):
                for k in range(0, len(processedList[j][1])):
                    gameName.setBlock(loc.x + cRPL[k], loc.y - 1, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), block.GOLD_BLOCK.id)
        elif configWay[1] == 4:      # flute timbre
            for j in range(0, hitNum):
                for k in range(0, len(processedList[j][1])):
                    gameName.setBlock(loc.x + cRPL[k], loc.y - 1, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), block.CLAY.id)
        elif configWay[1] == 5:      # chime timbre
            for j in range(0, hitNum):
                for k in range(0, len(processedList[j][1])):
                    gameName.setBlock(loc.x + cRPL[k], loc.y - 1, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), block.PACKED_ICE.id)
        elif configWay[1] == 6:      # guitar timbre
            for j in range(0, hitNum):
                for k in range(0, len(processedList[j][1])):
                    gameName.setBlock(loc.x + cRPL[k], loc.y - 1, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), block.WOOL.id)
        elif configWay[1] == 7:      # xylophone timbre
            for j in range(0, hitNum):
                for k in range(0, len(processedList[j][1])):
                    gameName.setBlock(loc.x + cRPL[k], loc.y - 1, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), block.BONE_BLOCK.id)

    if configWay[0] == 2:

        for j in range(0, hitNum):
            for k in range(0, len(processedList[j][1])):
                if 0 <= processedList[j][1][k] < 24:      # low range, use double bass timbre
                    gameName.setNoteBlock(loc.x + cRPL[k], loc.y, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), processedList[j][1][k])
                    gameName.setBlock(loc.x + cRPL[k], loc.y - 1, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), block.WOOD.id)
                if 24 <= processedList[j][1][k] < 48:      # medium range, use harp/piano timbre
                    gameName.setNoteBlock(loc.x + cRPL[k], loc.y, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), processedList[j][1][k] - 24)
                    gameName.setBlock(loc.x + cRPL[k], loc.y - 1, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), block.GRASS.id)
                if 48 <= processedList[j][1][k] <= 72:      # high range, use glockenspiel timbre
                    gameName.setNoteBlock(loc.x + cRPL[k], loc.y, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), processedList[j][1][k] - 48)
                    gameName.setBlock(loc.x + cRPL[k], loc.y - 1, loc.z + 4 + processedList[j][0] / minDelay * (2 + rN), block.GOLD_BLOCK.id)

# --------------------
# placeRepeater
# --------------------

def placeRepeater(loc, hitNum, minDelay, rN, cRPL, processedList, gameName):
    for i in range(0, len(cRPL)):
        for j in range(0, int(processedList[-1][0] / minDelay)):
            if int(minDelay % 4) == 0:
                gameName.setBlock(loc.x + cRPL[i], loc.y, loc.z + 6 + rN - 1 + j * (2 + rN), block.UNPOWERED_REPEATER.id, 2 + 12)      # delay = 4
            else:
                gameName.setBlock(loc.x + cRPL[i], loc.y, loc.z + 6 + rN - 1 + j * (2 + rN), block.UNPOWERED_REPEATER.id, 2 + 4 * (int(minDelay % 4) - 1))      # delay != 4
            for k in range(0, rN - 1):      # range(0, 0) = []
                gameName.setBlock(loc.x + cRPL[i], loc.y, loc.z + 6 + k + j * (2 + rN), block.UNPOWERED_REPEATER.id, 2 + 12)      # delay = 4
                # 2 means facing south (z-axis positive)

# --------------------
# placeRedstoneWire
# --------------------

def placeRedstoneWire(loc, hitNum, voiceMax, minDelay, rN, cRPL, processedList, gameName):
    
    for i in range(0, len(cRPL)):
        for j in range(0, int(processedList[-1][0] / minDelay)):
            gameName.setBlock(loc.x + cRPL[i], loc.y, loc.z + 5 + j * (2 + rN), block.REDSTONE_WIRE.id)
    
    # also place a redstone wire if "3 + processedList[j][0] / minDelay * (2 + rN)" has no note block because of note lacking on this specific voice
    for k in range(0, hitNum):
        for l in range(len(processedList[k][1]), voiceMax):
            gameName.setBlock(loc.x + cRPL[l], loc.y, loc.z + 4 + processedList[k][0] / minDelay * (2 + rN), block.REDSTONE_WIRE.id)

    for m in range(0, int(processedList[-1][0] / minDelay)):
        if m * minDelay not in [processedListMember[0] for processedListMember in processedList]:
            for n in range(0, len(cRPL)):
                gameName.setBlock(loc.x + cRPL[n], loc.y, loc.z + 4 + m * (2 + rN), block.REDSTONE_WIRE.id)

# --------------------
# placeTorch
# --------------------

def placeTorch(loc, zBoundary, hitNum, rN, cRPL, gameName):
    if hitNum == 1:
        for i in range(cRPL[0] - 1, cRPL[-1] + 2, 2):
            gameName.setBlock(loc.x + i, loc.y, loc.z + 3, block.TORCH.id)
    else:
        # place torch every three rows of repeaters
        for i in range(cRPL[0] - 1, cRPL[-1] + 2, 2):
            m = -3
            while True:
                m += 3
                if 6 + m * (2 + rN) >= zBoundary[1]:
                    break
                gameName.setBlock(loc.x + i, loc.y, loc.z + 6 + m * (2 + rN), block.TORCH.id)

# --------------------
# placeBaseLine
# --------------------

def placeBaseLine(loc, cRPL, gameName):
    # the base line can only spread redstone signal to 15 columns at most
    for i in range(cRPL[0], cRPL[-1]+1):
        gameName.setBlock(loc.x + i, loc.y, loc.z + 2, block.REDSTONE_WIRE.id)
    for j in range(0, len(cRPL)):
        gameName.setBlock(loc.x + cRPL[j], loc.y, loc.z + 3, block.UNPOWERED_REPEATER.id, 2)
    gameName.setBlock(loc.x, loc.y, loc.z + 1, block.WOODEN_BUTTON.id, 5)

# --------------------
# constructRedstoneSystem
# --------------------

def constructRedstoneSystem(cL, gameName):      # cL means configurationList

    gameName.postToChat("")
    gameName.postToChat("Please input (in-game) the name of the player beside whom the note block system is placed:")
    gameName.postToChat("")
    
    while True:
        posts = gameName.events.pollChatPosts()
        if len(posts) > 0:
            try:
                name = posts[0].message
                id = gameName.getPlayerEntityId(name)
            except mcpi.connection.RequestError:
                gameName.postToChat("")
                gameName.postToChat("Wrong name, please input again:")
                gameName.postToChat("")
                continue
            else:
                break
    
    loc = gameName.entity.getPos(id);

    gameName.postToChat("")
    gameName.postToChat("Attaching...")
    gameName.postToChat("This takes less than a minute for a medium-sized midi file.")
    gameName.postToChat("")

    # cL[0] is configWay, [1] is preProcessResult, [2] is columnRelativePlacingList, [3] is processedList
    # cL[1][0] is hitNum, [1][1] is voiceMax, [1][2] is minDelay, [1][3] is repeaterNum
    theXBoundary = xBoundary(cL[2])
    theZBoundary = zBoundary(cL[1][2], cL[1][3], cL[3])

    placeStone(loc, theXBoundary, theZBoundary, gameName)
    placeGlass(loc, theXBoundary, theZBoundary, gameName)
    placeAir(loc, theXBoundary, theZBoundary, gameName)
    placeDoor(loc, theZBoundary, gameName)

    placeNoteBlock(loc, cL[0], cL[1][0], cL[1][2], cL[1][3], cL[2], cL[3], gameName)
    placeRepeater(loc, cL[1][0], cL[1][2], cL[1][3], cL[2], cL[3], gameName)
    placeRedstoneWire(loc, cL[1][0], cL[1][1], cL[1][2], cL[1][3], cL[2], cL[3], gameName)
    placeBaseLine(loc, cL[2], gameName)

    placeTorch(loc, theZBoundary, cL[1][0], cL[1][3], cL[2], gameName)

    gameName.postToChat("Midi file successfully processed and attached in-game!")
    gameName.postToChat("If you wish to process another, reload the program.")
