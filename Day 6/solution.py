import re
turnon = "turn on"

turnoff = "turn off"

togg = "toggle"

fileName = "input.txt"

def createGrid():
    grid = []
    d = {}
    for i in range(0,1000):
        for j in range(0,1000):
            d[str([i,j])] = 0
            

    return d

def turnOn(line,d):
    line = line.split()
    startCoord = line[2]
    startCoord = startCoord.split(",")
    startRow = int(startCoord[0])
    startCol= int(startCoord[1])
    endCoord = line[4].split(",")
    endRow = int(endCoord[0])
    endCol= int(endCoord[1])

    for i in range(startRow,endRow +1):
        for j in range(startCol,endCol+1):
            d[str([i,j])] = 1
            


def turnOff(line,d):
    line = line.split()
    startCoord = line[2]
    startCoord = startCoord.split(",")
    startRow = int(startCoord[0])
    startCol= int(startCoord[1])
    endCoord = line[4].split(",")
    endRow = int(endCoord[0])
    endCol= int(endCoord[1])

    for i in range(startRow,endRow +1):
        for j in range(startCol,endCol+1):
            d[str([i,j])] = 0
            


def toggle(line,d):
    line = line.split()
    startCoord = line[1]
    startCoord = startCoord.split(",")
    startRow = int(startCoord[0])
    startCol= int(startCoord[1])
    endCoord = line[3].split(",")
    endRow = int(endCoord[0])
    endCol= int(endCoord[1])
    
    for i in range(startRow,endRow +1):
        for j in range(startCol,endCol+1):
            if d[str([i,j])] == 1:
                d[str([i,j])] = 0
            elif d[str([i,j])] == 0:
                d[str([i,j])] = 1


def part1():
    with open(fileName) as f:
        d = createGrid()
        result = 0
        for line in f:
            if turnon in line:
               turnOn(line,d)
            elif turnoff in line:
                turnOff(line,d)
            elif togg in line:
                toggle(line,d)

        for item in d:
            result += d[item]

        print(result)



def turnUp(line,d):
    line = line.split()
    startCoord = line[2]
    startCoord = startCoord.split(",")
    startRow = int(startCoord[0])
    startCol= int(startCoord[1])
    endCoord = line[4].split(",")
    endRow = int(endCoord[0])
    endCol= int(endCoord[1])

    for i in range(startRow,endRow +1):
        for j in range(startCol,endCol+1):
            d[str([i,j])] += 1
            


def turnDown(line,d):
    line = line.split()
    startCoord = line[2]
    startCoord = startCoord.split(",")
    startRow = int(startCoord[0])
    startCol= int(startCoord[1])
    endCoord = line[4].split(",")
    endRow = int(endCoord[0])
    endCol= int(endCoord[1])

    for i in range(startRow,endRow +1):
        for j in range(startCol,endCol+1):
            if d[str([i,j])] > 0:
                d[str([i,j])] -= 1
            


def toggleUp(line,d):
    line = line.split()
    startCoord = line[1]
    startCoord = startCoord.split(",")
    startRow = int(startCoord[0])
    startCol= int(startCoord[1])
    endCoord = line[3].split(",")
    endRow = int(endCoord[0])
    endCol= int(endCoord[1])
    
    for i in range(startRow,endRow +1):
        for j in range(startCol,endCol+1):  
            d[str([i,j])] += 2


def part2():
    with open(fileName) as f:
        d = createGrid()
        result = 0
        for line in f:
            if turnon in line:
               turnUp(line,d)
            elif turnoff in line:
                turnDown(line,d)
            elif togg in line:
                toggleUp(line,d)

        for item in d:
            result += d[item]

        print(result)

part2()
            
