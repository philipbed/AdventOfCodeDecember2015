import hashlib
key = "iwrupvqb"

success = "00000"
for i in range(0,1000000):
    copy = key
    copy += str(i)
    m = hashlib.md5()
    m.update(copy)
    h = m.hexdigest()
    if h[:5] == success:
        print(i)
        break
    
