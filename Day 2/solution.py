fileName = "dimensions.txt"

def calcWrapperPaper( length,width,height ):
    dimensionLst = [length,width,height]
    largestDim = max( dimensionLst )
    dimensionLst.remove( largestDim )

    surfaceArea = calcSurfaceArea( length,width,height )

    smallestArea = dimensionLst[0] * dimensionLst[1]

    return surfaceArea + smallestArea
    

def calcSurfaceArea(length,width,height):
    surfaceArea1 = 2*length*width
    surfaceArea2 = 2*length*height
    surfaceArea3 = 2*height*width

    return surfaceArea1 + surfaceArea2 + surfaceArea3

def part1():
    with open( fileName ) as f:
        result = 0
        for line in f:
            line = line.split( "x" )
            length = int(line[0])
            width = int(line[1])
            height = int(line[2])
            result += calcWrapperPaper( length, width ,height )
        print(result)

def perimeter( length,width ):

    return length + length +width +width

def calcVolume(length,width,height):

    return length * width * height

def calcRibbon(length,width,height):
    lst = [length,width,height]
    largestDim = max( lst )
    lst.remove( largestDim )

    smallestLength = lst[0]
    smallestWidth = lst[1]
    perim = perimeter( smallestLength, smallestWidth )
    volume = calcVolume( length,width,height )

    return perim + volume

def part2():
    with open( fileName ) as f:
        result = 0
        for line in f:
            line = line.split( "x" )
            length = int(line[0])
            width = int(line[1])
            height = int(line[2])
            result += calcRibbon( length, width ,height )
        print( result )

part2()
