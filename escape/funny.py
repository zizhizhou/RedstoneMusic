"""
Author: JerryLv
Theme: Funny 
"""
from escape.interface import *
import random
from mcpi import block
from mcpi import block,entity


class Funny(Level):
    LENGTH = 30
    HALFWIDTH = 4
    WIDTH = 2 * HALFWIDTH +1
    @staticmethod
    def exitWin(entrance: Window):
        dir = entrance.direction
        if dir == Dir.N:
            entrance.middle.z -= Funny.LENGTH
        elif dir == Dir.S:
            entrance.middle.z += Funny.LENGTH
        elif dir == Dir.E:
            entrance.middle.x += Funny.LENGTH
        elif dir == Dir.W:
            entrance.middle.x -= Funny.LENGTH
        entrance.height = 7
        return entrance

    def _construct(self):
        LENGTH = Funny.LENGTH
        setbs = self.mc.setBlocks
        x, y, z = self.entWin.middle
        WIDTH = self.entWin.width
        HEIGHT = self.entWin.height
        HALFWIDTH = Funny.HALFWIDTH
        WIDTHmy = Funny.WIDTH
        direction = self.entWin.direction
        
        wall = block.STONE_BRICK.id
        glass = block.GLASS.id
        trap1 = block.CACTUS.id
        gold = block.GOLD_BLOCK.id
        deco1 = block.DIAMOND_BLOCK.id
        deco2 = block.PUMPKIN.id
        sand = block.SAND.id
        air = block.AIR.id
        entity1 = entity.HORSE.id
        entity2 = entity.ENDERMAN.id
        
        
        if direction == Dir.E:
            ##主墙
            
            if WIDTH > WIDTHmy :
                setbs(x,y,z-WIDTH//2,x,y+HEIGHT,z+WIDTH//2,deco2)
                setbs(x,y,z-HALFWIDTH,x,y+7,z+HALFWIDTH,air)
            elif WIDTH < WIDTHmy :
                setbs(x,y,z-HALFWIDTH,x,y+7,z+HALFWIDTH,deco2)
                setbs(x,y,z-WIDTH//2,x,y+HEIGHT,z+WIDTH//2,air)
            
            
            setbs(x,y-1,z-HALFWIDTH-1,x+LENGTH,y-1,z+HALFWIDTH+1,wall)
            setbs(x,y-1,z-HALFWIDTH-1,x+LENGTH,y+7,z-HALFWIDTH-1,wall)
            setbs(x,y-1,z+HALFWIDTH+1,x+LENGTH,y+7,z+HALFWIDTH+1,wall)
            setbs(x,y+7,z-HALFWIDTH-1,x+LENGTH,y+7,z+HALFWIDTH+1,glass)
            setbs(x+3,y-2,z-HALFWIDTH,x+LENGTH-1,y-2,z+HALFWIDTH,wall) 
            setbs(x+3,y-1,z-HALFWIDTH,x+LENGTH-1,y-1,z+HALFWIDTH,sand) 
            
            setbs(x+1,y-1,z-HALFWIDTH,x+1,y-1,z+HALFWIDTH,gold)
            ##装饰线
            setbs(x+1,y+3,z-HALFWIDTH-1,x+LENGTH-1,y+3,z-HALFWIDTH-1,deco1)
            setbs(x+1,y+3,z+HALFWIDTH+1,x+LENGTH-1,y+3,z+HALFWIDTH+1,deco1)
            
            setbs(x,y-1,z-HALFWIDTH-1,x,y-1,z+HALFWIDTH+1,deco2)
            setbs(x,y-1,z-HALFWIDTH-1,x,y+6,z-HALFWIDTH-1,deco2)
            setbs(x,y-1,z+HALFWIDTH+1,x,y+6,z+HALFWIDTH+1,deco2)
            
            setbs(x+LENGTH,y-1,z-HALFWIDTH-1,x+LENGTH,y-1,z+HALFWIDTH+1,deco2)
            setbs(x+LENGTH,y-1,z-HALFWIDTH-1,x+LENGTH,y+6,z-HALFWIDTH-1,deco2)
            setbs(x+LENGTH,y-1,z+HALFWIDTH+1,x+LENGTH,y+6,z+HALFWIDTH+1,deco2)
            ##陷阱
            for m in range(0,9,2):
                
                for n in range(0,27,6):
                    setbs(x+3+n,y,z-HALFWIDTH+m,x+3+n,y+random.randint(0,1),z-HALFWIDTH+m,trap1)
            
            for m in range(1,8,2):
                
                for n in range(0,24,6):
                    P=random.randint(0,2)
                    setbs(x+6+n,y,z-HALFWIDTH+m,x+6+n,y+P,z-HALFWIDTH+m,trap1)
                    
                   
        elif direction == Dir.W:
            ##
            if WIDTH > WIDTHmy :
                setbs(x,y,z-WIDTH//2,x,y+HEIGHT,z+WIDTH//2,deco2)
                setbs(x,y,z-HALFWIDTH,x,y+7,z+HALFWIDTH,air)
            elif WIDTH < WIDTHmy :
                setbs(x,y,z-HALFWIDTH,x,y+7,z+HALFWIDTH,deco2)
                setbs(x,y,z-WIDTH//2,x,y+HEIGHT,z+WIDTH//2,air)
            
            
            setbs(x,y-1,z-HALFWIDTH-1,x-LENGTH,y-1,z+HALFWIDTH+1,wall)
            setbs(x,y-1,z-HALFWIDTH-1,x-LENGTH,y+7,z-HALFWIDTH-1,wall)
            setbs(x,y-1,z+HALFWIDTH+1,x-LENGTH,y+7,z+HALFWIDTH+1,wall)
            setbs(x,y+7,z-HALFWIDTH-1,x-LENGTH,y+7,z+HALFWIDTH+1,glass)
            setbs(x+3,y-1,z-HALFWIDTH,x-LENGTH+1,y-1,z+HALFWIDTH,sand)
            setbs(x+3,y-2,z-HALFWIDTH,x-LENGTH+1,y-2,z+HALFWIDTH,wall)
            setbs(x+3,y-1,z-HALFWIDTH,x-LENGTH+1,y-1,z+HALFWIDTH,sand)
            ##起跑线
            setbs(x,y-1,z-HALFWIDTH,x,y-1,z+HALFWIDTH,gold)
            setbs(x-1,y-1,z-HALFWIDTH,x-1,y-1,z+HALFWIDTH,gold)
            ##装饰线
            setbs(x-1,y+3,z-HALFWIDTH-1,x-LENGTH+1,y+3,z-HALFWIDTH-1,deco1)
            setbs(x-1,y+3,z+HALFWIDTH+1,x-LENGTH+1,y+3,z+HALFWIDTH+1,deco1)
            
            setbs(x,y-1,z-HALFWIDTH-1,x,y-1,z+HALFWIDTH+1,deco2)
            setbs(x,y-1,z-HALFWIDTH-1,x,y+6,z-HALFWIDTH-1,deco2)
            setbs(x,y-1,z+HALFWIDTH+1,x,y+6,z+HALFWIDTH+1,deco2)
            
            setbs(x-LENGTH,y-1,z-HALFWIDTH-1,x-LENGTH,y-1,z+HALFWIDTH+1,deco2)
            setbs(x-LENGTH,y-1,z-HALFWIDTH-1,x-LENGTH,y+6,z-HALFWIDTH-1,deco2)
            setbs(x-LENGTH,y-1,z+HALFWIDTH+1,x-LENGTH,y+6,z+HALFWIDTH+1,deco2)
            ##陷阱
          
            for m in range(0,9,2):
                
                for n in range(0,27,6):
                    setbs(x-3-n,y,z-HALFWIDTH+m,x-3-n,y,z-HALFWIDTH+m,trap1)
            for m in range(1,8,2):
                
                for n in range(0,24,6):
                    P=random.randint(0,2)
                    setbs(x-6-n,y,z-HALFWIDTH+m,x-6-n,y+P,z-HALFWIDTH+m,trap1)
                    
                    
        elif direction == Dir.N:
            ##主墙
          
            if WIDTH > WIDTHmy :
                setbs(x-WIDTH//2,y,z,x+WIDTH//2,y+HEIGHT,z,deco2)
                setbs(x-HALFWIDTH,y,z,x+HALFWIDTH,y+7,z,air)
            elif WIDTH < WIDTHmy :
                setbs(x-HALFWIDTH,y,z,x+HALFWIDTH,y+7,z,deco2)
                setbs(x-WIDTH//2,y,z,x+WIDTH//2,y+HEIGHT,z,air)
            
            
            setbs(x-HALFWIDTH-1,y-1,z,x+HALFWIDTH+1,y-1,z-LENGTH,wall)
            setbs(x-HALFWIDTH-1,y-1,z,x-HALFWIDTH-1,y+7,z-LENGTH,wall)
            setbs(x+HALFWIDTH+1,y-1,z,x+HALFWIDTH+1,y+7,z-LENGTH,wall)
            setbs(x-HALFWIDTH-1,y+7,z,x+HALFWIDTH+1,y+7,z-LENGTH,glass)
            setbs(x-HALFWIDTH,y-2,z-3,x+HALFWIDTH,y-2,z-LENGTH+1,wall)
            setbs(x-HALFWIDTH,y-1,z-3,x+HALFWIDTH,y-1,z-LENGTH+1,sand)
            ##起跑线
            setbs(x-HALFWIDTH,y-1,z-1,x+HALFWIDTH,y-1,z-1,gold)
            ##装饰线
            setbs(x-HALFWIDTH-1,y+3,z-1,x-HALFWIDTH-1,y+3,z-LENGTH+1,deco1)
            setbs(x+HALFWIDTH+1,y+3,z-1,x+HALFWIDTH+1,y+3,z-LENGTH+1,deco1)
            
            setbs(x-HALFWIDTH-1,y-1,z,x+HALFWIDTH+1,y-1,z,deco2)
            setbs(x-HALFWIDTH-1,y-1,z,x-HALFWIDTH-1,y+6,z,deco2)
            setbs(x+HALFWIDTH+1,y-1,z,x+HALFWIDTH+1,y+6,z,deco2)
            
            setbs(x-HALFWIDTH-1,y-1,z-LENGTH,x+HALFWIDTH+1,y-1,z-LENGTH,deco2)
            setbs(x-HALFWIDTH-1,y-1,z-LENGTH,x-HALFWIDTH-1,y+6,z-LENGTH,deco2)
            setbs(x+HALFWIDTH+1,y-1,z-LENGTH,x+HALFWIDTH+1,y+6,z-LENGTH,deco2)
            ##陷阱
            for m in range(0,9,2):
                
                for n in range(0,27,6):
                    setbs(x-HALFWIDTH+m,y,z-3-n,x-HALFWIDTH+m,y,z-3-n,trap1)
                    
            for m in range(1,8,2):
                
                for n in range(0,24,6):
                    P=random.randint(0,2)
                    setbs(x-HALFWIDTH+m,y,z-6-n,x-HALFWIDTH+m,y+P,z-6-n,trap1)
                    
        elif direction == Dir.S:
           ##主墙
            if WIDTH > WIDTHmy :
                setbs(x-WIDTH//2,y,z,x+WIDTH//2,y+HEIGHT,z,deco2)
                setbs(x-HALFWIDTH,y,z,x+HALFWIDTH,y+7,z,air)
            elif WIDTH < WIDTHmy :
                setbs(x-HALFWIDTH,y,z,x+HALFWIDTH,y+7,z,deco2)
                setbs(x-WIDTH//2,y,z,x+WIDTH//2,y+HEIGHT,z,air)
           
           
           
            setbs(x-HALFWIDTH-1,y-1,z,x+HALFWIDTH+1,y-1,z+LENGTH,wall)
            setbs(x-HALFWIDTH-1,y-1,z,x-HALFWIDTH-1,y+7,z+LENGTH,wall)
            setbs(x+HALFWIDTH+1,y-1,z,x+HALFWIDTH+1,y+7,z+LENGTH,wall)
            setbs(x-HALFWIDTH-1,y+7,z,x+HALFWIDTH+1,y+7,z+LENGTH,glass)
            setbs(x-HALFWIDTH,y-2,z+3,x+HALFWIDTH,y-2,z+LENGTH-1,wall)
            setbs(x-HALFWIDTH,y-1,z+3,x+HALFWIDTH,y-1,z+LENGTH-1,sand)
            ##起跑线
            setbs(x-HALFWIDTH,y-1,z+1,x+HALFWIDTH,y-1,z+1,gold)
            ##装饰线
            setbs(x-HALFWIDTH-1,y+3,z+1,x-HALFWIDTH-1,y+3,z+LENGTH-1,deco1)
            setbs(x+HALFWIDTH+1,y+3,z+1,x+HALFWIDTH+1,y+3,z+LENGTH-1,deco1)
            
            setbs(x-HALFWIDTH-1,y-1,z,x+HALFWIDTH+1,y-1,z,deco2)
            setbs(x-HALFWIDTH-1,y-1,z,x-HALFWIDTH-1,y+6,z,deco2)
            setbs(x+HALFWIDTH+1,y-1,z,x+HALFWIDTH+1,y+6,z,deco2)
            
            setbs(x-HALFWIDTH-1,y-1,z+LENGTH,x+HALFWIDTH+1,y-1,z+LENGTH,deco2)
            setbs(x-HALFWIDTH-1,y-1,z+LENGTH,x-HALFWIDTH-1,y+6,z+LENGTH,deco2)
            setbs(x+HALFWIDTH+1,y-1,z+LENGTH,x+HALFWIDTH+1,y+6,z+LENGTH,deco2)
            ##陷阱
            for m in range(0,9,2):
                
                for n in range(0,27,6):
                    setbs(x-HALFWIDTH+m,y,z+3+n,x-HALFWIDTH+m,y,z+3+n,trap1)
                    
            for m in range(1,8,2):
                
                for n in range(0,24,6):
                    P=random.randint(0,2)
                    setbs(x-HALFWIDTH+m,y,z+6+n,x-HALFWIDTH+m,y+P,z+6+n,trap1)

    def _loop(self):
        """静态关卡"""
        pass

    def _cleanup(self):
        pass
