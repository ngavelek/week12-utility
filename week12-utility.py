#https://github.com/ngavelek/week12-utility/commits/master
#Nate Gavelek
#CSCI 102 - Section C
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

def Union(list1, list2):
    return list1 + list2

def Intersection(list1, list2):
    overLapList = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            print (list1[i], list2[j])
            if list1[i] == list2[j]:
               overLapList.append(list1[i])

    return overLapList


