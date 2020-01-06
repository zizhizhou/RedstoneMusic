import sys
sys.path.append("..")
import time
import tools
mc=tools.start(0)
pId=mc.getPlayerEntityIds()[0]
while True:
    setsand=mc.setBlock(mc.entity.getTilePos(pId),12)
    time.sleep(1)