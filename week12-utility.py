#Nate Gavelek
#CSCI 102
#week12-utility -- Incremental build model

def PrintOutput(whatToPrint):
    print("OUTPUT", whatToPrint)

def LoadFile (filename):
    file = open(filename)
    fRead = file.read()
    return fRead.split('\n')

def UpdateString(string1, string2, index):
    updatedString = ''
    makeList = list(string1)
    for i in range(len(makeList)):
        makeList[index] = string2
    for i in makeList:
        updatedString += i
    print(updatedString)

def FindWordCount(list, string):
    makeString = str(list)
    counter = makeString.count(string)
    return counter

def ScoreFinder(listNames, listFloats, playerFind):
    foundPlayer = False
    for i in range(len(listNames)):
        if playerFind.capitalize() == listNames[i]:
            print("OUTPUT", playerFind, "got a score of 6")
            foundPlayer = True
    if foundPlayer == False:
        print("OUTPUT player not found")


