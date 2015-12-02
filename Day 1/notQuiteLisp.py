fileName = "floorMoves.txt"
def findDifferece():
    openParen = 0
    closeParen = 0
    with open(fileName) as f:
        for line in f:
            for ch in line:
                if ch == "(":
                    openParen += 1
                elif ch == ")":
                    closeParen += 1
        return abs(openParen - closeParen)

def findFloorNegOne():
    floor = 0
    position = 1
    with open( fileName ) as f:
        for line in f:
            for ch in line:
                if ch == "(":
                    floor += 1
                elif ch == ")":
                    if floor == 0:
                        return position
                    floor -= 1

                position += 1

    

