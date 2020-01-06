import sys, random
sys.path.append("..")
import tools
def setblock(x,y,z):
    '''create a block with ladders,input position and id of the block in the middle'''
    mc.setBlock(x,y,z,45)
    mc.setBlock(x+1,y,z,65,5)
    mc.setBlock(x-1,y,z,65,4)
    mc.setBlock(x,y,z+1,65,3)
    mc.setBlock(x,y,z-1,65,2)
    
mc=tools.start(0)
setb=mc.setBlock
setbs=mc.setBlocks
pId=mc.getPlayerEntityIds()[0]
start=mc.entity.getTilePos(pId)
x=start.x
y=start.y
z=start.z
length=int(input('halflength='))#输入关卡宽度的一半
height=int(input('height='))#输入关卡高度
setbs(x-length,y,z-length,x+length,0,z+length,0)
for i in range(x-length,x+length,3):
    for j in range(y-3,y+height,3):
        for k in range(z-length,z+length,3):
            m=random.randint(0,3)
            setblock(i+m,j+m,k+m)
