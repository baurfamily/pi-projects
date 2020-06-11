from mcpi.minecraft import Minecraft
import mcpi.block as block
from random import randint
from time import sleep

class Wall:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.was_near_block = False
        self.distance = 2
            
    def checkDistance(self, source, target, epsilon=0):
        return source >= target - epsilon and source <= target + epsilon
    
    def isNear(self, x, z):
        return self.checkDistance(self.x, x, self.distance) and self.checkDistance(self.z, z, self.distance)
    
    def show(self):
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y+1, self.z, block.STONE)
    
    def hide(self):
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y+1, self.z, block.AIR)

mc = Minecraft.create()

w = Wall(0, 8, 12)


while True:
    ppos = mc.player.getTilePos()
    if w.isNear(ppos.x, ppos.z):
        if not w.was_near_block:
            w.show()
            print('your on the block')
            mc.postToChat('your on the block')
            w.was_near_block = True
    else:
        if w.was_near_block:
            w.hide()
            print('you moved away')
            mc.postToChat('you moved away')
            w.was_near_block = False