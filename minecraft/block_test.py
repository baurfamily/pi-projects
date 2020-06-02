from mcpi.minecraft import Minecraft
import mcpi.block as block
from random import randint
from time import sleep

mc = Minecraft.create()

x, y, z = 0, 8, 12

was_near_block = False

def checkDistance(source, target, epsilon=0):
    return source >= target - epsilon and source <= target + epsilon

while True:
    ppos = mc.player.getTilePos()
    if checkDistance(ppos.x, x, 1) and checkDistance(ppos.z, z, 1):
        if not was_near_block:
            print('your on the block')
            mc.postToChat('your on the block')
            was_near_block = True
    else:
        if was_near_block:
            print('you moved away')
            mc.postToChat('you moved away')
            was_near_block = False