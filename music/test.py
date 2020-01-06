import sys
import math
sys.path.append("..")

import mcpi.minecraft as mmc
import readMidiFile as rmf
import tools

mc=tools.start(0)

i=0
interval=2
x=1
j=0
width=0
max_width=0
pre_x=0

print("请输入midi文件路径")
filename=input()

print("请输入游戏用户名")
playername=input()
id=mc.getPlayerEntityId(playername)
coordinate=mc.entity.getTilePos(id)
#print(coordinate)
_x=0
_y=0
_z=0

print("请选择模式（输入序号）：\n"
      "1.音符优先：程序将尽可能还原每一个音符，当然，节奏将不会被保证\n"
      "2.节奏优先：程序将尽可能还原原曲节奏，部分音符可能会被省略")
mode=input()

for bpm,note_value,pitches in rmf.musical_extract_midi(filename):

    if i==0:
        _x=coordinate.x-len(pitches)-1
        _y=coordinate.y-4
        _z=coordinate.z+2
        mc.setBlocks(_x-3,_y+4,_z+i+interval,_x+2*len(pitches)+4,_y+4,_z+i-2,98)
        mc.setBlock(_x+len(pitches)+1,_y+5,_z-1,77,7)
        print("处理中……")
        
    if width>max_width:
        max_width=width


 
    #if bpm>150:
        #bpm=150
    x=600.0*note_value/bpm+pre_x
    #print(x)
    if mode=="2" and x<0.5 and i!=0:
        pre_x=x
        continue
    x=round(x)
    pre_x=0
    if x<1:
        x=1

        
    interval=x+1
    #y=x
    j=0
   
    mc.setBlocks(_x-5,_y+5,_z+i+1,_x+2*len(pitches),_y+11,_z+i+20,0) 
    i=i+interval
    mc.setBlocks(_x-3,_y+4,_z+i,_x+2*max_width+4,_y+4,_z+i-x,98)
    for k in pitches:
        j=j+1

        if k<30:
            k=30
        elif k>102:
            k=102
        if k>=30 and k<54:
            if k>=30 and k<42:
                mc.setBlock(_x+2*j,_y+5,_z+i,17)
                mc.setNoteBlock(_x+2*j,_y+6,_z+i,(k+18)%24)
                #bass-wood

            else:
                mc.setBlock(_x+2*j,_y+4,_z+i,98)
                mc.setBlock(_x+2*j,_y+5,_z+i,12)
                mc.setNoteBlock(_x+2*j,_y+6,_z+i,(k+6)%12)
                #sand-snare drum


        elif k>=54 and k<78:

            if k>=54 and k<66:
                mc.setBlock(_x+2*j,_y+4,_z+i,98)
                mc.setBlock(_x+2*j,_y+5,_z+i,12)
                mc.setNoteBlock(_x+2*j,_y+6,_z+i,(k+6)%24)
                #sand-snare drum

            else:
                mc.setBlock(_x+2*j,_y+5,_z+i,3)
                mc.setNoteBlock(_x+2*j,_y+6,_z+i,(k+18)%24)
                #piano-dirt

        elif k>=78:
            mc.setBlock(_x+2*j,_y+5,_z+i,1)
            mc.setNoteBlock(_x+2*j,_y+6,_z+i,(k+22)%25)
        #click-stone           
        mc.setBlock(_x+2*j-1,_y+5,_z+i,123)
    mc.setBlock(_x+2*j+1,_y+5,_z+i,123)
    #音符盒


     


    while x!=0:
        for z in range(len(pitches)):
            mc.setBlock(_x+2*(z+1),_y+5,_z+i+x-interval,93,2)
        x=x-1

    """            
    if x>0:
        for z in range(len(pitches)):
            mc.setBlock(2*(z+1),5,i+y-interval,93,2+4*(x-1))
    """
#中继器

          
    if len(pitches)>width:
        mc.setBlocks(_x+2*width+1,_y+5,_z+i-interval,_x+2*len(pitches),_y+5,_z+i-interval,55)
#红石

    width=len(pitches)     

        

#mc.setBlocks(-3,5,0,-3,10,i+4,20)
#mc.setBlocks(2*max_width+4,5,0,2*max_width+4,10,i+4,20)
print("完成")


