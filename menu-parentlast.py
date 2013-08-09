from maya.cmds import *

#1. make an array of all selected objects
target = ls(sl=True)

#2. parent each selected object to the last object
for i in range(0,len(target)-1):
    select(target[i])
    parent(target[i],target[len(target)-1])


#3. select last object
select(target[len(target)-1])