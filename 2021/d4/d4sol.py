inFile = open('input.txt', 'r').read().split('\n')
data = []
count = 0

drawn_numbers = inFile[0].split(',')
drawn_numbers = [int(x) for x in drawn_numbers]
print(drawn_numbers)
inFile = inFile[1:]
for line in inFile:
    if line:
        board = {}
        num = line.split()
        num = [int(x) for x in num]
        for n in num:
            board[n] = False
        #board[num] = False
        #print(f'line {[line]}, board : {board}')
        data.append(board)


#print(data)
#print(bingo_bricks)

def make_bingo_board(data):
    global drawn_numbers
    #print(drawn_numbers)
    bingo_boards = []
    #print(f'data0: {data[0]}, data1: {data[1]}')
    while data:
        board = []
        #print(f'data: {data[:5]}')
        bingo_boards.append(data[:5])
        data = data[5:]

    for board in bingo_boards:
        #print(board) 
        #[[{'24': False, '96': False, '27': False, '39': False, '3': False}], 
        #[{'54': False, '26': False, '12': False, '65': False, '60': False}],
        #[{'67': False, '62': False, '43': False, '98': False, '14': False}], 
        #[{'15': False, '95': False, '2': False, '82': False, '33': False}],
        #[{'64': False, '17': False, '86': False, '0': False, '63': False}]]
        """for row in board:
            print(row)
            for item in row:
                #{'64': False, '17': False, '86': False, '0': False, '63': False}
                print(item)
                for key, val in item.items():
                    #64 False
                    # 17 False
                    # 86 False
                    # 0 False
                    # 63 False
                    print(key, val)"""

        #print("\n")

    #print(bingo_boards)

    return drawn_numbers, bingo_boards


def draw_and_mark(board, number):

    print(f'board: {board}, number: {number} \n')
    for row in board:
        for key, val in row.items():
            #print(f'key: {key}')
            if key == number:
                row[key] = True
                print(f'Changed row[0][number]: {key, number, row[key]} \n {row}')
    
    return board
    
    

if __name__ == '__main__':

    drawn_numbers, bingo_boards = make_bingo_board(data)
    for board in bingo_boards:
        print(f'drawn: {int(drawn_numbers[0])}')
        #Draw number
        board = draw_and_mark(board, int(drawn_numbers[0]))
        #Check if bingo
        #If bingo: board --> winning board, break
        #else continue. CHeck next drawn_num
    drawn_numbers = drawn_numbers[1:]

    print(bingo_boards)