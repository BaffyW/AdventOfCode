inFile = open('input.txt', 'r').read().split('\n')
data = []
count = 0

for line in inFile:
    data.append(line)

def decode(instructions):
    horizontal = 0
    depth = 0

    for inst in instructions:
        if inst:
            code = inst.split()
            command = code[0]
            val = int(code[1])
            #print(f'code: {code[0]}, X: {code[1]}')
            match command:
                case 'forward':
                    horizontal += val
                case 'down':
                    depth += val
                case 'up':
                    depth -= val
    print(f'horizontal: {horizontal}, depth: {depth}')
    return horizontal * depth


def decode_part_two(instructions):
    horizontal = 0
    depth = 0
    aim = 0

    for inst in instructions:
        if inst:
            code = inst.split()
            command = code[0]
            val = int(code[1])
            #print(f'code: {code[0]}, X: {code[1]}')
            match command:
                case 'forward':
                    horizontal += val
                    depth += aim * val
                case 'down':
                    aim += val
                case 'up':
                    aim -= val
    print(f'horizontal: {horizontal}, depth: {depth}')
    return horizontal * depth



if __name__ == '__main__':
    #print(data)
    #data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    print(decode(data))
    print(decode_part_two(data))

