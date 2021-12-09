from os import linesep

inFile = open('input.txt', 'r').read().split('\n')
data = []
count = 0

for line in inFile:
    data.append(line)


def get_gamma_rate(data): #most common
    gamma_rate = []
    width = len(data[0])
    for i in range(width):
        i_list = []
        #print(i)
        for row in data:
            if row:
                i_list.append(row[i])
        #print(i_list)
        gamma_rate.append(max(set(i_list), key=i_list.count))
        #print(gamma_rate)
    gamma_rate = "".join(gamma_rate)
    return gamma_rate


def get_epsilon_rate(gamma): #least common
    epsilon = []
    for bit in gamma:
        epsilon.append(str(int(not int(bit))))
    epsilon = "".join(epsilon)
    return epsilon
    

def part_two(data):
    oxygen_gen = []
    CO2 = []
    width = len(data[0])
    ox_keep_list = data
    co2_keep_list = data
    keep_list = data
    #print(data, len(data))

    """for i in range(width):
        ox_passing = []
        co2_passing = []
        ox_i_list = [num[i] for num in ox_keep_list]
        co2_i_list = [num[i] for num in co2_keep_list]
        most = (max(set(ox_i_list), key=ox_i_list.count))
        least = (min(set(co2_i_list), key = co2_i_list.count))

        for num in keep_list:
            #print(i, num, most, num[i] == most)
            if num[i] == most:
                passing.append(num)
        keep_list = passing
        oxygen_gen = passing
    print(f'oxygen_gen: {oxygen_gen}')"""

    
    for i in range(width):
        i_list = [num[i] for num in keep_list]
     
        #print(i_list, len(i_list))

        passing = []
        #i_list = [num[i] for num in keep_list]
        most = int((max(i_list, key=i_list.count)))
        least  = int((min(i_list, key=i_list.count)))

        if most == least:
            #print("most = least")
            most = 1

        for num in keep_list:
            #print(i, num, num[i], most, int(num[i]) == most)
            if int(num[i]) == most:
                passing.append(num)
                #print(f'appending {num}')
        keep_list = passing
        oxygen_gen = passing
        if len(passing) == 1:
            break
    print(f'oxygen_gen: {oxygen_gen}')

    #print("LEAST______________________")
    keep_list = data
    for i in range(width):
        i_list = [num[i] for num in keep_list]
        passing = []

        most = int((max(i_list, key=i_list.count)))
        least  = int((min(i_list, key=i_list.count)))

        if most == least:
            least = 0

        for num in keep_list:
            #print(i, num, num[i], least, int(num[i]) == least)
            if int(num[i]) == least:
                passing.append(num)
        #print(f'{i} keeping: {passing}')
        keep_list = passing
        CO2 = passing
        if len(passing) == 1:
            break
    print(f'CO2: {CO2}')
    #x = '0'
    #print(int(x))
    
    return int(oxygen_gen[0], 2), int(CO2[0], 2)


def rec_count(keep_list):
    if len(keep_list) == 1:
        pass



def get_dec_from_bin(bin):
    return int(bin, 2)

if __name__ == '__main__':
    #data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    print(data[:-1])
    #gamma = get_gamma_rate(data)
    #print(gamma)
    #epsilon = get_epsilon_rate(gamma)
    #print(epsilon)
    
    #gamma_dec = get_dec_from_bin(gamma)
    #epsilon_dec = get_dec_from_bin(epsilon)
    #print(gamma_dec, epsilon_dec, gamma_dec * epsilon_dec)

    ox, co2 = part_two(data[:-1])
    #ox = get_dec_from_bin(ox)
    #co2 = get_dec_from_bin(co2)
    #ox = list(map(int, ox))
    print(ox, co2, ox*co2)

    #life_supp = ox * co2
    #print(life_supp)
    


