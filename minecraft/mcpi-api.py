#!/usr/bin/python3

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

# get player position
pPos = mc.player.getTilePos()

mc.postToChat("API Test!")

# change block
print("Create stone 3x3 cube")
mc.setBlocks(pPos.x-1, pPos.y, pPos.z-1, pPos.x+1, pPos.y+2, pPos.z+1, block.STONE)

print("Position player on top")
mc.player.setPos(pPos.x, pPos.y+3, pPos.z)

mc.postToChat("Move and have another go")