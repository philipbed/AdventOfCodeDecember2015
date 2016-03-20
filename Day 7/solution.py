fileName = "input.txt"
NOT = "NOT"
AND = "AND"
OR = "OR"
LS = "LSHIFT"
RS = "RSHIFT"
s = 65535

def som(d):
    for key in d:
        val = d[key]
        if type(val) != int:
            if AND in val:
                lst = val.split(",")
                one = lst[0]
                two = lst[2]
                if type(d[one]) == int:
                    if type(d[two]) == int:
                        d[key] = d[one] & d[two]
            elif OR in val:
                lst = val.split(",")
                one = lst[0]
                two = lst[2]
                if type(d[one]) == int:
                    if type(d[two]) == int:
                        d[key] = d[one] | d[two]
            elif RS in val:
                    lst = val.split(",")
                    one = lst[0]
                    two = int(lst[2])
                    if type(d[one]) == int:
                        d[key] = d[one] >> two
            elif NOT in val:
                    lst = val.split(",")
                    one = lst[1]
                    if type(d[one]) == int:
                        d[key] = s - d[one] 
            elif LS in val:
                    lst = val.split(",")
                    one = lst[0]
                    two = int(lst[2])
                    if type(d[one]) == int:
                        d[key] = d[one] << two
                    
                

def part1():
    with open('test.txt') as f:
    #with open(fileName) as f:
        d = {}
        for line in f:
            line = line.split()
            if NOT in  line:
                
                key = line[1]
                otherKey = line[3]
                if key not in d:
                    d[otherKey] = NOT+","+key
                elif key in d and type(d[key]) == int:
                    d[otherKey] = s - d[key]
                else:
                    d[otherKey] = NOT+","+key
                    
            elif OR in line:
                keyOne = line[0]
                keyTwo = line[2]
                otherKey = line[4]
                if keyOne not in d and keyTwo not in d:
                    d[otherKey] = keyOne+","+OR+","+keyTwo
                elif keyOne in d and type(d[keyOne]) == int:
                    if keyTwo in d and type(d[keyTwo]) == int:
                        d[otherKey] = d[keyOne] | d[keyTwo]
                    else:
                        d[otherKey] = keyOne+","+OR+","+keyTwo
                else:
                    d[otherKey] = keyOne+","+OR+","+keyTwo
      
            elif AND in line:
                keyOne = line[0]
                keyTwo = line[2]
                otherKey = line[4]
                if keyOne not in d and keyTwo not in d:
                    d[otherKey] = keyOne+","+AND+","+keyTwo
                elif keyOne in d and type(d[keyOne]) == int:
                    if keyTwo in d and type(d[keyTwo]) == int:
                        d[otherKey] = d[keyOne] & d[keyTwo]
                    else:
                        d[otherKey] = keyOne+","+AND+","+keyTwo
                    
                else:
                    d[otherKey] = keyOne+","+AND+","+keyTwo

            elif LS in line:
                keyOne = line[0]
                shiftVal = line[2]
                otherKey = line[4]
                if keyOne not in d:
                    d[otherKey] = keyOne+","+LS+","+shiftVal
                elif keyOne in d and type(d[keyOne]) == int:
                    d[otherKey] = d[keyOne] << int(shiftVal)
                else:
                    d[otherKey] = keyOne+","+LS+","+shiftVal

            elif RS in line:
                keyOne = line[0]
                shiftVal = line[2]
                otherKey = line[4]
                if keyOne not in d:
                    d[otherKey] = keyOne+","+RS+","+shiftVal
                elif keyOne in d and type(d[keyOne]) == int:
                    d[otherKey] = d[keyOne] >> int(shiftVal)
                else:
                    d[otherKey] = keyOne+","+RS+","+shiftVal

            else:
            
                val = line[0]
                if val.isdigit():
                    key = line[2]
                    d[key] = int(val)
                else:
                    key = line[2]
                    d[key] = val
        print(d)
        for item in d:
            if type(d[item])
        som(d)
        print(d)

part1()
