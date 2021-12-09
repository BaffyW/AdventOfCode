inFile = open("input.txt")
data = []
count = 0

for line in inFile:
    line.split("\n")
    data.append(int(line))

def count_amount_of_increases(data):
    #global data
    global count
    #print(data)
    #data = [123, 126, 130, 137, 140, 150, 155, 157, 173, 186]
    #data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    prev = data[0]
    data = data[1:]
    l = len(data)
    print(l)
    for i in range(l):
        if data[i] > prev:
            count += 1
        if i < 50:
            pass
            #print(f'i: {i}, vals: {prev, data[i]}, increase: {prev and data[i] > prev}')
        prev = data[i]

    print(count)

def make_three_meas_windows():
    global data
    #data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    group_data = []
    for i in range (len(data)-2):
        first = data[i]
        second = data[i+1]
        third = data[i+2]

        s = first + second + third
        group_data.append(s)
    print(group_data)
    count_amount_of_increases(group_data)

            





if __name__  == '__main__':
    #count_amount_of_increases()
    make_three_meas_windows()