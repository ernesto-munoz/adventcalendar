from pprint import pprint


OBSTACLE = "#"

def get_in_front_position(position:tuple, orientation:int) -> tuple:
    new_position:tuple = None
    match orientation:
        case 0:
            new_position = (position[0] - 1, position[1])
        case 1:
            new_position = (position[0], position[1] + 1)
        case 2:
            new_position = (position[0] + 1, position[1])
        case 3:
            new_position = (position[0], position[1] - 1)
    return new_position

def is_out_bounds(lab:list[list], position:tuple) -> bool:
    width, height = len(lab[0]), len(lab)
    if position[0] < 0 or position[1] < 0 or position[0] >= height or position[1] >= width:
        return True
    
    return False
    

def walk(lab:list[list], start_position:tuple, orientation:int = 0) -> list[list]:
    walk_map:list[list] = lab.copy()
    pprint(walk_map)
    
    curr_position = start_position
    curr_orientation = orientation
    
    while True:
        new_position = get_in_front_position(position=curr_position, orientation=curr_orientation)
        if is_out_bounds(lab, new_position) is True:
            lab[curr_position[0]][curr_position[1]] = "X"
            break
        in_front:str = lab[new_position[0]][new_position[1]]
        if in_front == OBSTACLE:
            curr_orientation = (curr_orientation + 1) % 4
        else:
            lab[curr_position[0]][curr_position[1]] = "X"
            curr_position = new_position
        
    
    return walk_map

def count_steps(lab:list[list]) -> int:
    total_steps = 0
    for row in lab:
        total_steps += row.count("X")
    return total_steps
        

def main() -> None:
    lab = list()
    start_row, start_column = None, None
    with open("test.txt") as f:
        i = 0
        for line in f:
            line = line.rstrip()
            lab.append(list(line))
            if (j := line.find("^")) != -1:
                start_row = i
                start_column = j
            i += 1
            
    walked_map = walk(lab, (start_row, start_column))
    pprint(walked_map)
    steps_num = count_steps(walked_map)
    print(f"Positions occupied: {steps_num}")
    
            


    
if __name__ == "__main__":
    main()