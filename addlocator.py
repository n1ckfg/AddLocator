from maya.cmds import *

#1. make an array of all selected objects
target = ls(sl=True)

#2. if no selection, just make a locator at 0,0,0...
if(len(target)==0):
	spaceLocator()

else:
	#3. otherwise, for each selected object...
	for i in range(0,len(target)):
		
		#4. ...if there are child joints, give them locators too
		try:
			kids = listRelatives(ls(selection=True), children=True, type="joint", allDescendents=True)
			for k in kids:
				locName = k + "_loc"
				locPos = xform(k, q=True, t=True, ws=True)
		   		loc = spaceLocator(n=locName)
		   		move(locPos[0],locPos[1],locPos[2])
		except:
			print "No child joints."

		#5. get the original selection's name
		locName = target[i] + "_loc"
		
		#6. get its position
		locPos = xform(target[i], q=True, t=True, ws=True)
		
		#7. create a new locator with that name at that position
		loc = spaceLocator(n=locName)
		move(locPos[0],locPos[1],locPos[2])