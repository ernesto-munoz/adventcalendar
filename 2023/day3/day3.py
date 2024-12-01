import string

def get_numbers_positions(schematic) -> list:
    columns = len(schematic[0])
    rows = len(schematic)
    data = list()
    for r in range(0, rows):
        c = 0
        while c < columns:
            if schematic[r][c] in string.digits:
                for cc in range(c + 1, columns):
                    if schematic[r][cc] not in string.digits:
                        break
                else:
                    cc = cc + 1
                data.append(
                    {
                        "begin": (r, c),
                        "end": (r, cc - 1)
                    }
                )
                c = cc
            c += 1
    return data

def is_adjacent(number_position, schematic) -> bool:
    up_row = number_position["begin"][0] - 1
    same_row = number_position["begin"][0]
    down_row = number_position["begin"][0] + 1
    
    if up_row >= 0:
        for c in range(number_position["begin"][1] - 1, number_position["end"][1] + 2):
            if 0 <= c < len(schematic[up_row]):
                if schematic[up_row][c] not in string.digits + ".":
                    return True

    if down_row < len(schematic):
        for c in range(number_position["begin"][1] - 1, number_position["end"][1] + 2):
            if 0 <= c < len(schematic[down_row]):
                if schematic[down_row][c] not in string.digits + ".":
                    return True
            
    if 0 < number_position["end"][1] < len(schematic[same_row]) - 1:
        if schematic[same_row][number_position["begin"][1] - 1] not in string.digits + ".":
            return True

        if schematic[same_row][number_position["end"][1] + 1] not in string.digits + ".":
            return True
        
    return False

def get_adjacents(number_position, schematic) -> list:
    up_row = number_position["begin"][0] - 1
    same_row = number_position["begin"][0]
    down_row = number_position["begin"][0] + 1
    adjacents = list()
    
    if up_row >= 0:
        for c in range(number_position["begin"][1] - 1, number_position["end"][1] + 2):
            if 0 <= c < len(schematic[up_row]):
                if schematic[up_row][c] not in string.digits + ".":
                    adjacents.append((schematic[up_row][c], up_row, c))

    if down_row < len(schematic):
        for c in range(number_position["begin"][1] - 1, number_position["end"][1] + 2):
            if 0 <= c < len(schematic[down_row]):
                if schematic[down_row][c] not in string.digits + ".":
                    adjacents.append((schematic[down_row][c], down_row, c))
            
    if 0 < number_position["end"][1] < len(schematic[same_row]) - 1:
        if schematic[same_row][number_position["begin"][1] - 1] not in string.digits + ".":
            adjacents.append((schematic[same_row][number_position["begin"][1] - 1], same_row, number_position["begin"][1] - 1))

        if schematic[same_row][number_position["end"][1] + 1] not in string.digits + ".":
            adjacents.append((schematic[same_row][number_position["end"][1] + 1], same_row, number_position["end"][1] + 1))
        
    return adjacents
    
def get_number(position, schematic):
    row = position["begin"][0]
    column = position["begin"][1]
    l = position["end"][1] - position["begin"][1] + 1
    
    return schematic[row][column:column + l]

def main() -> None:
    total = 0
    gear_ratio = 0
    schematic = list()
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            schematic.append(line)

    number_positions = get_numbers_positions(schematic=schematic)
    previously_in_position = dict()
    for each_number_position in number_positions:
        if is_adjacent(each_number_position, schematic=schematic) is True:
            total += int(get_number(each_number_position, schematic=schematic))

        adjacents = get_adjacents(each_number_position, schematic=schematic)
        for each_adjacent in adjacents:
            if each_adjacent[0] == "*":
                if (each_adjacent[1], each_adjacent[2]) in previously_in_position:
                    previously_in_position[(each_adjacent[1], each_adjacent[2])].append(int(get_number(each_number_position, schematic=schematic)))
                else:
                    previously_in_position[(each_adjacent[1], each_adjacent[2])] = [int(get_number(each_number_position, schematic=schematic))]
                
    for p in previously_in_position:
        if len(previously_in_position[p]) == 2:
            gear_ratio += previously_in_position[p][0] * previously_in_position[p][1]
    
    print(f"Total: {total}")
    print(f"Gear Ratio: {gear_ratio}")
            

if __name__ == "__main__":
    main()
    # {'begin': (24, 137), 'end': (24, 138)} False 76