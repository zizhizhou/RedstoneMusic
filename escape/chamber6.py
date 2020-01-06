import sys
sys.path.append("..")
import tools,random
mc=tools.start(0)
setbs=mc.setBlocks
pId = mc.getPlayerEntityId(map(mc.entity.getName, mc.getPlayerEntityIds()))
start = mc.entity.getTilePos(pId)
direction=input('the direction is: ')
WIDTH=10
LENGTH=20
BLOCK_ID=57
x=start.x
y=start.y
z=start.z
if direction=='e':
    setbs(x+1,y,z-WIDTH//2,x+LENGTH+1,0,z+WIDTH//2,0)
    for i in range(x+2,x+LENGTH-1,4):
        for j in range(z-WIDTH//2+1,z+WIDTH//2-1,4):
            m = random.randint(0,4)
            setbs(i+m-1,y-1,j+m-1,i+m,y-1,j+m,213)
elif direction=='w':
    setbs(x-1,y,z-WIDTH//2,x-LENGTH-1,0,z+WIDTH//2,0)
    for i in range(x-LENGTH+1,x-2,4):
        for j in range(z-WIDTH//2+1,z+WIDTH//2-1,4):
            m = random.randint(0,4)
            setbs(i+m-1,y-1,j+m-1,i+m,y-1,j+m,213)
elif direction=='n':
    setbs(x-WIDTH//2,y,z-1,x+WIDTH//2,0,z-LENGTH-1,0)
    for i in range(z-LENGTH+1,z-2,4):
        for j in range(x-WIDTH//2+1,x+WIDTH//2-1,4):
            m = random.randint(0,4)
            setbs(j+m-1,y-1,i+m-1,j+m,y-1,i+m,213)
elif direction=='s':
    setbs(x-WIDTH//2,y,z+1,x+WIDTH//2,0,z+LENGTH+1,0)
    for i in range(z+2,z+LENGTH-1,4):
        for j in range(x-WIDTH//2+1,x+WIDTH//2-1,4):
            m = random.randint(0,4)
            setbs(j+m-1,y-1,i+m-1,j+m,y-1,i+m,213)
