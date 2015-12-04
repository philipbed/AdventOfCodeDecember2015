import hashlib


key = "iwrupvqb"



def part1():
    part1Check= "00000"
    oneMillion = 1000000
    for i in range(100000,oneMillion):
        copy = key
        copy += str(i)
        m = hashlib.md5()
        m.update(copy)
        h = m.hexdigest()
        if h[:5] == part1Check:
            print(i)
            break
    
def part2():
    part2Check = "000000"
    tenMillion = 10000000
    for i in range(1000000,tenMillion):
        copy = key
        copy += str(i)
        m = hashlib.md5()
        m.update(copy)
        h = m.hexdigest()
        if h[:6] == part2Check:
            print(i)
            break
part1()
part2()
