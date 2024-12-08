from pprint import pprint

def get_antennas_frequency_position(antennas_map:list[list]) -> dict:
    """Map with each frequencia and the positions of the antennas"""
    frequencies = dict()
    for r in range(len(antennas_map)):
        for c in range(len(antennas_map[r])):
            if antennas_map[r][c] != ".":
                if antennas_map[r][c] in frequencies.keys():
                    frequencies[antennas_map[r][c]].append((r, c))
                else:
                    frequencies[antennas_map[r][c]] = [(r, c)]
    return frequencies            
    
def get_antinodes_position(a:tuple, b:tuple) -> list:
    """For a couple of antennas, get the antinodes"""
    man_distance:tuple = (abs(a[0] - b[0]), abs(a[1] - b[1]))
            
    left_antinode_x = a[0] - man_distance[0] if a[1] < b[1] else b[0] + man_distance[0]
    left_antinode_y = min(a[1], b[1]) - man_distance[1]
    
    right_antinode_x = a[0] - man_distance[0] if a[1] > b[1] else b[0] + man_distance[0]
    right_antinode_y = max(a[1], b[1]) + man_distance[1]

    return [(left_antinode_x, left_antinode_y), (right_antinode_x, right_antinode_y)]

def get_antinodes_position_advanced(a:tuple, b:tuple, max_length:int) -> list:
    """For a couple of antennas, get the antinodes in all the range (max_length)"""
    man_distance:tuple = (abs(a[0] - b[0]), abs(a[1] - b[1]))
    positions = list()
    
    for i in range(1, max_length + 1):
        
        left_antinode_x = a[0] - man_distance[0] * i if a[1] < b[1] else b[0] + man_distance[0] * i
        left_antinode_y = min(a[1], b[1]) - man_distance[1] * i
        positions.append((left_antinode_x, left_antinode_y))
        
        right_antinode_x = a[0] - man_distance[0] * i if a[1] > b[1] else b[0] + man_distance[0] * i
        right_antinode_y = max(a[1], b[1]) + man_distance[1] * i
        positions.append((right_antinode_x, right_antinode_y))

    return positions

def is_valid_position(antennas_map:list[list], pos:tuple) -> bool:
    """Check if the position is valid in the map"""
    if pos[0] >= 0 and pos[0] < len(antennas_map) and pos[1] >= 0 and pos[1] < len(antennas_map[0]):
        return True
    return False

def get_all_antinodes_positions(antennas_map:list[list]) -> list:
    """Get all the antonides positions of the map"""
    antennas_frequency_position = (get_antennas_frequency_position(antennas_map))
    antinodes = set()
    for frequency in antennas_frequency_position.keys():
        positions = antennas_frequency_position[frequency]
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                antinodes_positions = get_antinodes_position(positions[i], positions[j])
                for antinode_position in antinodes_positions:
                    if is_valid_position(antennas_map, antinode_position) is True:
                        antinodes.add(antinode_position)

    return antinodes

def get_all_antinodes_positions_advanced(antennas_map:list[list]) -> list:
    """Get all the antinodes positions of the map (extended length)"""
    antennas_frequency_position = (get_antennas_frequency_position(antennas_map))
    antinodes = set()
    for frequency in antennas_frequency_position.keys():
        positions = antennas_frequency_position[frequency]
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                antinodes_positions = get_antinodes_position_advanced(positions[i], positions[j], len(antennas_map) * len(antennas_map[0]))
                for antinode_position in antinodes_positions:
                    if is_valid_position(antennas_map, antinode_position) is True and antennas_map[antinode_position[0]][antinode_position[1]] == ".":
                        antinodes.add(antinode_position)

    return antinodes


def get_antinodes_map(antennas_map:list[list], antinodes:list[tuple]) -> list[list]:
    """Get a representation of the map with the antinodes marked with #"""
    antinodes_map = antennas_map.copy()
    
    for antinode in antinodes:
        antinodes_map[antinode[0]][antinode[1]] = "#"
    return antinodes_map

def map_to_string(map:list[list]) -> str:
    return "\n".join(["".join(r) for r in map])

def get_num_antennas(antennas_map:list[list]) -> int:
    """Get the number of antennas in the map"""
    num = 0
    for r in range(len(antennas_map)):
        for c in range(len(antennas_map[r])):
            if antennas_map[r][c] != ".":
                num += 1
    return num

def main() -> None:
    
    antennas_map: list = list()
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip()
            antennas_map.append([_ for _ in line])
    
    num_antennas = get_num_antennas(antennas_map)
    antinodes_locations: list = get_all_antinodes_positions(antennas_map)
    antinodes_locations_advanced: list = get_all_antinodes_positions_advanced(antennas_map)
    print(map_to_string(get_antinodes_map(antennas_map, antinodes_locations_advanced)))
    print(f"Num. of antinodes: {len(antinodes_locations)}")
    print(f"Num. of antinodes(advanced): {len(antinodes_locations_advanced) + num_antennas}")
    
if __name__ == "__main__":
    main()