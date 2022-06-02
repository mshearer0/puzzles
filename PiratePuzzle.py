#!/usr/bin/env python

numbersteps = 5
numberislands = 5
allpiratewalks = []

targetwalk = [2,3,4,2,3,4]

# given a walk as a list of island numbers
# return a list of possible walks with an additional step 
def nextsteps(walk):
    newwalks = []
    nextlist = nextislands(walk[-1])
    for next in range(len(nextlist)):
        newwalk = walk[:]
        newwalk.append(nextlist[next])
        newwalks.append(newwalk)
    return newwalks
    
# given an island number 
# return list of possible next island numbers
def nextislands(currentisland):
    nextoptions = []
    if currentisland+1 <= numberislands:
        nextoptions.append(currentisland+1)
    if currentisland-1 > 0:
        nextoptions.append(currentisland-1)
    return nextoptions

# for all starting islands and number of steps calculate all the possible walks as list of lists of island numbers
for startisland in range(1,numberislands+1):
    piratewalks = [[startisland]]
    for step in range(numbersteps):
        newwalks = []
        for walks in range(len(piratewalks)):
            extendwalks = nextsteps(piratewalks[walks])
            newwalks.extend(extendwalks)
        piratewalks = newwalks        
    allpiratewalks.extend(piratewalks)
    
# check target answer against all possible walks
for walks in range(len(allpiratewalks)):
    foundpirate = False
    for step in range(len(allpiratewalks[walks])):
        if allpiratewalks[walks][step] == targetwalk[step]:
            foundpirate = True
            break
    if foundpirate == False:
        print("Pirate Escaped")
        print(allpiratewalks[walks])
        print(targetwalk)
       
# print(allpiratewalks)
