inFile = open("map.txt")
data = []
h = 1
for line in inFile:
    data.append(line)
    h+=1

def traverse(x_slope, y_slope):
    counter = 0
    x = 0
    y = 0

    print("h: ", h)

    for row in data:
        if(y > h):
            print("ROW: ", y)
            if(row[x] == '#'):
                counter +=1
            break
        #print(y, x, row)
        length = len(row) - 1
        #print(length)
        #print(y, x)
        if(row[x] == '#'):
            counter +=1
        x += x_slope
        if( x > length - 1):
            x = x - length
        y += y_slope
    return counter

def findAllSlopes():
    a = traverse(1, 1)
    b = traverse(3, 1) #274
    c = traverse(5, 1)
    d = traverse(7, 1)
    e = traverse(1, 2)

    print(a, b, c, d, e)
    return (a*b*c*d*e)
    #print(b)

mult = findAllSlopes()
#print(traverse(3, 1))
print(mult)