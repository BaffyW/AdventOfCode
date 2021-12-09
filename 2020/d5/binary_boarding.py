import re

inFile = open("boarding_passes.txt")
data = []
rows = list(range(0, 128))
columns = list(range(0, 8))
seatId = []


#Behöver egentligen inte binärkoda
def binaryCodePasses():
    count = 0
    """L = 0, R = 1, F = 0, B = 1"""
    for line in inFile:
        count += 1
        coded = ""
        for char in line:
            if (char == 'L'):
                coded += "0"
            elif (char == 'R'):
                coded += "1"
            elif (char == 'F'):
                coded += "0"
            elif (char == 'B'):
                coded += "1"
        #print("Coded: " + coded)
        data.append(coded)

    #print("count: " + str(count))
            

def binary_boarding():
    #Plocka ut de 7 första siffrorna och kolla binärträdet.
    #splice

    for line in data:
        search = rows
        for element in range(0, 7):
            length = len(search)
            mid_i = length//2 #Floor division

            if int(line[element]) == 0:
                search = search[:mid_i]
            else:
                search = search[mid_i:]
        row = search

        search = columns
        for element in range(7, 10):
            length = len(search)
            mid_i = length//2

            if int(line[element]) == 0:
                search = search[:mid_i]
            else:
                search = search[mid_i:]
        col = search

        tempId = row[0] * 8 + col[0]
        seatId.append(tempId)
    
    print(sorted(seatId))
    print("MAX = ", max(seatId))
    print("MIN = ", min(seatId))

def find_seat():
    sorted_seatId = sorted(seatId)
    count = 8
    for seat in sorted_seatId:
        print("Seat: ", seat)
        if(not seat == count):
            print("My seat: ", count)
            break
        count += 1

binaryCodePasses()
binary_boarding()
find_seat()