
fileName = "input.txt"
vowels = "aeiou"
bad1 = "ab"
bad2 = "cd"
bad3 = "pq"
bad4 = "xy"
badLst = [bad1,bad2,bad3,bad4]

def howManyVowels(line):
    count = 0
    for ch in line:
        if ch in vowels:
            count +=1
    return count
            
def isBad(line):
    for val in badLst:
        if val in line:
            return True
    return False

def hasDouble(line):
    count =0
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            count+=1
    return count >= 1

def part1():
    count = 0
    with open(fileName) as f:
        for line in f:
            if  not isBad(line):
                if howManyVowels(line) >= 3:
                    if hasDouble(line):
                        count += 1
        print(count)

def isOverlap(line):
    for i in range(len(line)-1):
        first = line[i]
        second = line[i+1]
        newString = first + second
        if line.count(newString) >= 2:
            return False

    return True

def isRepeated(line):
    for i in range(len(line)-2):
        first = line[i]
        second = line[i+1]
        third = line[i+2]
        if first == third:
            if second != third and second != first:
                return True

    return False

            
        

def part2():
    count = 0
    with open(fileName) as f:
        for line in f:
            if  not isOverlap(line):
                if isRepeated(line):
                    count += 1
        print(count)

part2()
