fileName = "floorMoves.txt"
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

                
print( findFloorNegOne() )
