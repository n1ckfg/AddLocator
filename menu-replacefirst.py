from maya.cmds import *

#1. make an array of all selected objects
target = ls(sl=True)

#2. for each selected object after the first...
for i in range(1,len(target)):

	#3. duplicate the first selection
	select(target[0])
	duplicate()

	#4. ...get the position
	pos = xform(target[i], q=True, t=True, ws=True)
    
	
	#5. move to position
	move(pos[0],pos[1],pos[2])

	#6. delete selection
	delete(target[i])
