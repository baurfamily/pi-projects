from mcpi.minecraft import Minecraft
import mcpi.block as block
from random import randint
from time import sleep

class Wall:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.was_near_block = False
        self.distance = 5
            
    def checkDistance(self, source, target, epsilon=0):
        return source >= target - epsilon and source <= target + epsilon
    
    def isNear(self, x, z):
        return self.checkDistance(self.x, x, self.distance) and self.checkDistance(self.z, z, self.distance)
    
    def show(self):
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y+1, self.z, block.STONE)
    
    def hide(self):
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y+1, self.z, block.AIR)
        
    def updateState(self, x, z):
        if self.isNear(x, z):
            if not self.was_near_block:
                self.show()
                self.was_near_block = True
        else:
            if self.was_near_block:
                self.hide()
                self.was_near_block = False

mc = Minecraft.create()

walls = []

for i in range(50):
    walls.append( Wall(-20+i, 8, 12) )

while True:
    ppos = mc.player.getTilePos()
    for w in walls:
        w.updateState(ppos.x, ppos.z)