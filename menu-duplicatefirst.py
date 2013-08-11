from maya.cmds import *
import maya.mel as mel

#1. make an array of all selected objects
target = ls(sl=True)

#2. if only one selection, just make a new duplicate at the same coordinates...
if(len(target)==1):
    #call through mel because python has no rc option!
    mel.eval("duplicate -un -ic -rc")

else:
    #3. ...otherwise, for each selected object...
    for i in range(1,len(target)):

        #4. ...get current selection's position and copy keyframes
        select(target[i])
        pos = xform(target[i], q=True, t=True, ws=True)
        try:
            copyKey()
        except:
            print "Couldn't copy keys."

        #5. duplicate the first selection
        select(target[0])
        #call through mel because python has no rc option!
        mel.eval("duplicate -un -ic -rc")
        
        #6. move first selection to position and paste keyframes
        move(pos[0],pos[1],pos[2])
        try:
            pasteKey()
        except:
            print "Couldn't paste keys."
           
        #7. delete selection
        delete(target[i])
