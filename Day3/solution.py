filenName = "input.txt"

def howManyHouses():
    count =0
    howMany = 1
    with open(fileName) as f:
        prev = ""
        for line in f:
            for ch in line:
                curr = ch
                if curr == ">":
                    if prev == "<":
                        pass
                    else:
                        howMany += 1
                elif curr == "<":
                    if prev == ">":
                        pass
                    else:
                        howMany += 1
                elif curr == "^":
                    if prev == "v":
                        pass
                    else:
                        howMany += 1
                else:
                    if prev == "<":
                        pass
                    else:
                        howMany += 1

class Coordinate(
