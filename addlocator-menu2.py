from maya.cmds import *

#1. make an array of all selected objects
target = ls(sl=True)

#2. for each selected object...
for i in range(0,len(target)):
	
	#3. ...get its name
	locName = target[i] + "_loc"
	
	#4. get its position
	locPos = xform(target[i], q=True, t=True, ws=True)
	
	#5. create a new locator with that name at that position
	loc = spaceLocator(n=locName)
	move(locPos[0],locPos[1],locPos[2])

	#6. make the locator a child of the selected object.
	parent(loc, target[i])