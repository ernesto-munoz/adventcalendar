VERTICAL_PIPE = "|"
HORIZONTAL_PIPE ="-"
NE_BEND = "L"
NW_BEND = "J"
SW_BEND = "W"
SE_BEND = "F"
GROUND = "."
STARTING_POSITION = "S"

NORTH = [VERTICAL_PIPE, SW_BEND, SE_BEND]
SOUTH = [VERTICAL_PIPE, NE_BEND, NW_BEND]
WEST = [HORIZONTAL_PIPE, NE_BEND, SE_BEND]
EAST = [HORIZONTAL_PIPE, NW_BEND, SW_BEND]


def get_starting_position(maze:list) -> (int, int):
    for row in range(0, len(maze)):
        for column in range(0, len(maze[row])):
            if maze[row][column] == STARTING_POSITION:
                return (row, column)
            
def possible_come_from_next_positions(maze:list, current_position:tuple) -> list:
    positions = list()
    
    rows = len(maze)
    columns = len(maze[0])
    
    north = (current_position[0] - 1, current_position[1])
    south = (current_position[0] + 1, current_position[1])
    west = (current_position[0], current_position[1] - 1)
    east = (current_position[0], current_position[1] + 1)
    
    if 0 <= north[0] <= rows - 1 and 0 <= north[1] <= columns - 1 and maze[north[0]][north[1]] in NORTH:
        positions.append(north)
        
    if 0 <= south[0] <= rows - 1 and 0 <= south[1] <= columns - 1 and maze[south[0]][south[1]] in SOUTH:
        positions.append(south)
        
    if 0 <= west[0] <= rows - 1 and 0 <= west[1] <= columns - 1 and maze[west[0]][west[1]] in WEST:
        positions.append(west)
        
    if 0 <= east[0] <= rows - 1 and 0 <= east[1] <= columns - 1 and maze[east[0]][east[1]] in EAST:
        positions.append(east)
    
    return positions

def possible_go_to_next_positions(maze:list, current_position:tuple) -> list:    
    positions = list()
    
    rows = len(maze)
    columns = len(maze[0])
    
    north = (current_position[0] - 1, current_position[1])
    south = (current_position[0] + 1, current_position[1])
    west = (current_position[0], current_position[1] - 1)
    east = (current_position[0], current_position[1] + 1)
    
    if 0 <= north[0] <= rows - 1 and 0 <= north[1] <= columns - 1 and maze[current_position[0]][current_position[1]] in SOUTH:
        positions.append(north)
        
    if 0 <= south[0] <= rows - 1 and 0 <= south[1] <= columns - 1 and maze[current_position[0]][current_position[1]] in NORTH:
        positions.append(south)
        
    if 0 <= west[0] <= rows - 1 and 0 <= west[1] <= columns - 1 and maze[current_position[0]][current_position[1]] in EAST:
        positions.append(west)
        
    if 0 <= east[0] <= rows - 1 and 0 <= east[1] <= columns - 1 and maze[current_position[0]][current_position[1]] in WEST:
        positions.append(east)
    
    return positions
    
    
# def move(maze, position, depth, starting_position):
#     next_positions = possible_go_to_next_positions(maze=maze, current_position=position)
#     for each_next_position in next_positions:
#         if each_next_position == starting_position:
#             continue
#         maze[position[0]][position[1]] = depth
#         # if depth < 2:
#         move(maze=maze, position=each_next_position, depth=depth + 1, starting_position=starting_position)

def search_loop(maze:list, position:tuple, already_visited:list) -> (bool, list):
    
    if maze[position[0]][position[1]] == STARTING_POSITION:
        next_positions = possible_come_from_next_positions(maze=maze, current_position=position)
    else:
        next_positions = possible_go_to_next_positions(maze=maze, current_position=position)

    for each_next_position in next_positions:
        if each_next_position not in already_visited:
            already_visited.append(each_next_position)
            if maze[each_next_position[0]][each_next_position[1]] == STARTING_POSITION:
                return True, [each_next_position]

            found, path = search_loop(maze=maze, position=each_next_position, already_visited=already_visited)
            if found is True:
                return found, [each_next_position] + path
    
    return False, []
        
    

def main() -> None:
    farthest_distance = 0
    maze = list()
    with open('./day10/test.txt') as f:
        for line in f:
            maze.append([SW_BEND if x == "7" else x for x in list(line.rstrip())])
    [print(x) for x in maze]
    

    starting_position = get_starting_position(maze=maze)
    # move(maze=maze, position=starting_position, depth=0, starting_position=starting_position)
    # to_analyze_positions = [starting_position]
    # distance = 0
    # while len(to_analyze_positions) > 0:
    #     position = to_analyze_positions.pop()
    #     maze[position[0]][position[1]] = distance
    #     next_positions = possible_next_positions(maze=maze, current_position=position)
    #     if starting_position in next_positions:
    #         next_positions.remove(starting_position)
    #     to_analyze_positions.extend(next_positions)
    #     distance += 1
    a, b = search_loop(maze=maze, position=starting_position, already_visited=[])
    print(a)
    print(b)
    
    print(f"Starting Position: {starting_position}")
    print(f"Farthest Distance: {farthest_distance}")
    # print(possible_go_to_next_positions(maze=maze, current_position=(2,1)))
    
    
    
            

if __name__ == "__main__":
    main()
    # 54697