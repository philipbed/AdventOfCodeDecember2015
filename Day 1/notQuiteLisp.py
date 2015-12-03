fileName = "floorMoves.txt"
def findDifferece():
    floor = 0
    with open( fileName ) as f:
        for line in f:
            for ch in line:
                if ch == "(":
                    floor += 1
                elif ch == ")":
                    floor += 1
        return floor

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

    

