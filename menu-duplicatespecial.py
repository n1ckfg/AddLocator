from maya.cmds import *
import maya.mel as mel

#1. make an array of all selected objects
target = ls(sl=True)

#2. for each selected object...
for i in range(0,len(target)):
    #3. ...select and duplicated with bones and keyframes
    select(target[i])
    #call through mel because python has no rc option!
    mel.eval("duplicate -un -ic -rc")
