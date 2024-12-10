from pprint import pprint

def get_starting_positions(height_map:list[list]) -> list[tuple]:
    """Get all the starting points (trailheads)"""
    starts = list()
    for r in range(len(height_map)):
        for c in range(len(height_map[r])):
            if height_map[r][c] == 0:
                starts.append((r, c))
    return starts

def get_all_possible_trails(height_map:list[list], position:tuple) -> list[list]:
    """Recusively get the trails from that position til the height 9. Can be done dinamically."""
    r, c = position[0], position[1]
    if height_map[r][c] == 9:
        return [[(r, c)]]

    trails = list()
    for row_dis, column_disp in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # possible movements
        new_r, new_c = r + row_dis, c + column_disp
        # out of bounds
        if new_r < 0 or new_c < 0 or new_r >= len(height_map) or new_c >= len(height_map[0]):
            continue
        if height_map[new_r][new_c] == height_map[r][c] + 1:
            found_trails = get_all_possible_trails(height_map, (new_r, new_c))
            for trail in found_trails:
                trail.append((r, c))
                trails.append(trail)
                
    return trails

def get_score(hiking_trails:list[list]) -> int:
    """Get the score of the trails (the trailhead). Number of different points with height 9."""
    endings = set()
    for hiking_trail in hiking_trails:
        endings.add(hiking_trail[0])
    return len(endings)

def get_rating(hiking_trails:list[list]) -> int:
    """Get the rating of the trails (the trailhead). Number of differents ways to reach points with a height 9."""
    return len(hiking_trails)

def main() -> None:    
    height_map = list()
    with open("input.txt") as f:
        for line in f:
            height_map.append([int(_) for _ in line.rstrip()])

    starts = get_starting_positions(height_map)
    total_score, total_rating = 0, 0
    for start in starts:
        trails = get_all_possible_trails(height_map, start)
        total_score += get_score(trails)
        total_rating += get_rating(trails)
    print(f"Total Score {total_score}")
    print(f"Total Rating {total_rating}")
    

    
    
if __name__ == "__main__":
    main()