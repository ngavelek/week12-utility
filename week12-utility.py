#Nate Gavelek
#CSCI 102
#week12-utility -- Incremental build model

def PrintOutput(whatToPrint):
    print("OUTPUT", whatToPrint)

def LoadFile (filename):
    file = open(filename)
    fRead = file.read()
    return fRead.split('\n')
