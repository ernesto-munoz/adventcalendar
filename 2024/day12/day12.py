from pprint import pprint

def search_region_in_position(garden:list[list[str]], position:tuple, visited_plots: list[bool]) -> list[tuple]:
    region = [position]
    visited_plots[position[0]][position[1]] = True
    for desp in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_position = (position[0] + desp[0], position[1] + desp[1])
        if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(garden) or new_position[1] >= len(garden[0]):
            continue
        if garden[position[0]][position[1]] == garden[new_position[0]][new_position[1]] and visited_plots[new_position[0]][new_position[1]] == False:
            region.extend(search_region_in_position(garden, new_position, visited_plots))
    return region

def search_regions(garden:list[list[str]]):
    rows, columns = len(garden), len(garden[0])
    pprint(garden)
    visited_plots = [[False] * len(row) for row in garden]
    pprint(visited_plots)
    regions = list()
    for r in range(rows):
        for c in range(columns):
            if visited_plots[r][c] == False:
                regions.append(search_region_in_position(garden, (r, c), visited_plots))
    pprint(regions)
    return regions

# def get_cluster_starts(regions:list[list]):
#     return [_[0] for _ in regions]

def get_region_area(region:list[tuple]) -> int:
    return len(region)

def get_region_perimeter(garden:list[list[str]], region:list[tuple]) -> int:
    start = region[0]
    symbol = garden[start[0]][start[1]]
    fences = 0
    for pos in region:
        for desp in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_position = (pos[0] + desp[0], pos[1] + desp[1])
            if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(garden) or new_position[1] >= len(garden[0]):
                fences += 1
            elif garden[new_position[0]][new_position[1]] != symbol:
                fences += 1
    return fences

def get_number_sides(garden:list[list[str]], region:list[tuple]) -> int:
    start = region[0]
    symbol = garden[start[0]][start[1]]
    fences = list()
    for pos in region:
        for desp in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_position = (pos[0] + desp[0], pos[1] + desp[1])
            if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(garden) or new_position[1] >= len(garden[0]):
                fences.append(new_position)
            elif garden[new_position[0]][new_position[1]] != symbol:
                fences.append(new_position)
    
    num_fences = 0
    while len(fences) > 0:
        
        # num_fences += 1
        # for other in fences:
        #     if fence[0] == other[0] or fence[1] == other[1]:
                
        fence = fences[0]
        for dim in [0, 1]:
            cross_region = False
            for pos in region:
                if pos[dim] == fence[dim]:
                    cross_region = True
                    break
            if cross_region is False:
                print(f"Use: f{fence}")
                removed = False
                for other in fences:
                    if fence[dim] == other[dim]:
                        fences.pop(0)
                        removed = True
                if removed is False:
                    num_fences += 1
                # fences = [other for other in fences if fence[dim] != other[dim]]
                
    
    return num_fences

def main() -> None:    
    garden = list()
    with open("test.txt") as f:
        for line in f:
            garden.append(list(line.strip()))
            
    regions = search_regions(garden)
    # starts =  get_cluster_starts(regions)
    price1 = 0
    price2 = 0
    for region in regions:
        area = get_region_area(region)
        perimeter = get_region_perimeter(garden, region)
        num_sides = get_number_sides(garden, region)
        print(f"Zone: {garden[region[0][0]][region[0][1]]} Area: {area} Perimeter: {perimeter} Num Sides: {num_sides}")
        price1 += area * perimeter
        price2 += area * num_sides
        
        
    print(f"Total price (area*perimeter): {price1}")
    print(f"Total price (area*num sides) Not working: {price2}")
    
    
if __name__ == "__main__":
    main()