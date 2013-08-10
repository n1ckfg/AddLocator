from maya.cmds import *

#1. make an array of all selected objects
target = ls(sl=True)

#2. for each selected object after the first...
for i in range(1,len(target)):

    #3. ...get current selection's position and copy keyframes
    select(target[i])
    pos = xform(target[i], q=True, t=True, ws=True)
    try:
        copyKey()
    except:
        print "Couldn't copy keys."

    #4. duplicate the first selection
    select(target[0])
    duplicate()
    
    #5. move first selection to position and paste keyframes
    move(pos[0],pos[1],pos[2])
    try:
        pasteKey()
    except:
        print "Couldn't paste keys."
       
    #6. delete selection
    delete(target[i])
