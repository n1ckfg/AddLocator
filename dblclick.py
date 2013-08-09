from maya.cmds import *

#1. make an array of all selected objects
target = ls(sl=True)

#2. get the position of the last selected object
pos = xform(target[len(target)-1], q=True, t=True, ws=True)

#3. move the other objects to the last selected object
for i in range(0,len(target)-1):
    select(target[i])
    move(pos[0],pos[1],pos[2])