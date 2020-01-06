import sys, random
sys.path.append("..")
import tools, time
mc=tools.start(0)
setbs=mc.setBlocks
setb=mc.setBlock

def area(x,y,z,direction,lenth,halfwide,num):
    '''输入起始坐标，方向，宽度的一半，一次落下铁砧的数量'''
    pos={}
    if direction=='s':
        setbs(x-halfwide,y-1,z,x+halfwide,y-1,z+lenth,159,4)
        setbs(x-halfwide-1,y-1,z,x-halfwide-1,y+10,z+lenth,235)
        setbs(x+halfwide+1,y-1,z,x+halfwide+1,y+10,z+lenth,235)
        for m in range(0,num):
            i=random.randint(x-halfwide,x+halfwide)
            j=random.randint(z,z+lenth)
            pos[m]=[i,y,j]
    elif direction=='n':
        setbs(x-halfwide,y-1,z,x+halfwide,y-1,z-lenth,159,4)
        setbs(x-halfwide-1,y-1,z,x-halfwide-1,y+10,z-lenth,235)
        setbs(x+halfwide+1,y-1,z,x+halfwide+1,y+10,z-lenth,235)
        for m in range(0,num):
            i=random.randint(x-halfwide,x+halfwide)
            j=random.randint(z-lenth,z)
            pos[m]=[i,y,j]
    elif direction=='w':
        setbs(x,y-1,z-halfwide,x-lenth,y-1,z+halfwide,159,4)
        setbs(x,y-1,z-halfwide-1,x-lenth,y+10,z-halfwide-1,235)
        setbs(x,y-1,z+halfwide+1,x-lenth,y+10,z+halfwide+1,235)
        for m in range(0,num):
            i=random.randint(z-halfwide,z+halfwide)
            j=random.randint(x-lenth,x)
            pos[m]=[j,y,i]
    elif direction=='e':
        setbs(x,y-1,z-halfwide,x+lenth,y-1,z+halfwide,159,4)
        setbs(x,y-1,z-halfwide-1,x+lenth,y+10,z-halfwide-1,235)
        setbs(x,y-1,z+halfwide+1,x+lenth,y+10,z+halfwide+1,235)
        for m in range(0,num):
            i=random.randint(z-halfwide,z+halfwide)
            j=random.randint(x,x+lenth)
            pos[m]=[j,y,i]
    return pos

def flash(x,y,z,direction,lenth,halfwide,num):
    '''输入起始坐标，方向，宽度的一半，一次落下铁砧的数量'''
    pos=area(x,y,z,direction,lenth,halfwide,num)
    FLASH_PERIOD=0.5
    FLASH_TIMES=3
    i=0
    while i<FLASH_TIMES:
        for m in range(0,num):
            setb(pos[m][0],pos[m][1]-1,pos[m][2],159,4) # yellow clay
        time.sleep(FLASH_PERIOD)
        for m in range(0,num):
            setb(pos[m][0],pos[m][1]-1,pos[m][2],159,14) # red clay
        time.sleep(FLASH_PERIOD)
        for m in range(0,num):
            if i==1:setb(pos[m][0],pos[m][1]+4,pos[m][2],145) # anvil
        i+=1
    
pId=mc.getPlayerEntityIds()[0]
dire=input('direction:')
wide=int(input('halfwide:'))
length=int(input('length:'))
start=mc.entity.getTilePos(pId)
num=length//4
while True:
    flash(start.x,start.y,start.z,dire,length,wide,num)
