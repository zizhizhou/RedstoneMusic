import sys
sys.path.append("..")

import mcpi.minecraft as mmc
import mcpi.block as block
import tools
from random import choice

mc = tools.start(0)

def testPlaceNoteBlock():
    mc.postToChat("Please input (in-game) the name of the player beside whom the note block system is placed:")
    # name = str(mc.events.pollChatPosts())
    # name = input()
    
    while True:
        posts = mc.events.pollChatPosts()
        if len(posts) > 0:
            try:
                name = posts[0].message
                id = mc.getPlayerEntityId(name)
            except BaseException:
                mc.postToChat("Wrong name, please input again:")
                continue
            else:
                break
    
    loc = mc.entity.getPos(id)
    # new_loc = [loc.x, loc.y, loc.z + 1]
    
    mc.setNoteBlock(loc.x, loc.y, loc.z + 1, 1)      # G pitch
    mc.setBlock(loc.x+1, loc.y, loc.z + 1, block.REDSTONE_WIRE.id)
    
    buttonIDList = [block.STONE_BUTTON.id, block.WOODEN_BUTTON.id] # 1.12.2 doesn't have buttons of other tree variants
    randomButtonID = choice(buttonIDList)
    mc.setBlock(loc.x + 2, loc.y, loc.z + 1, randomButtonID, 5)
    
    mc.postToChat("Congratulations! A note block with G pitch has been placed beside " + str(name) + ", together with a redstone circuit. Toggle the button to activate the note block!")