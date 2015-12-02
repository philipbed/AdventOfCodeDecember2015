fileName = "dimensions.txt"

def calcWrapperPaper(length,width,height):
    lst = [length,width,height]
    largestDim = max(lst)
    lst.remove(largestDim)

    surfaceArea = calcSurfaceArea(length,width,height)

    smallestArea = lst[0] * lst[1]

    return surfaceArea + smallestArea
    

def calcSurfaceArea(length,width,height):
    area1 = 2*length*width
    area2 = 2*length*height
    area3 = 2*height*width

    return area1 + area2 + area3

def part1():
    with open(fileName) as f:
        result = 0
        for line in f:
            line = line.split("x")
            result += calcWrapperPaper(int(line[0]),int(line[1]),int(line[2]))
        print(result)

def perimeter(length,width):

    return length + length +width +width

def calcVolume(length,width,height):

    return length * width * height

def calcRibbon(length,width,height):
    lst = [length,width,height]
    largestDim = max(lst)
    lst.remove(largestDim)

    return perimeter(lst[0],lst[1]) + calcVolume(length,width,height)

def part2():
    with open(fileName) as f:
        result = 0
        for line in f:
            line = line.split("x")
            result += calcRibbon(int(line[0]),int(line[1]),int(line[2]))
        print(result)

part2()
