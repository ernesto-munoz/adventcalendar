def search_in_direction(soup: list[str], row: int, column: int, direction: tuple[int, int], word:str="XMAS") -> bool:
    """Search the word in the char matrix in the given direction"""
    nr, nc = row, column
    for l in word:
        if nr < 0 or nr >= len(soup) or nc < 0 or nc >= len(soup[0]):
            return False
        if soup[nr][nc] != l:
            return False
        # next position
        nr += direction[0]
        nc += direction[1]
    return True

def search_xmas(soup: list[str]) -> int:
    """Search the word XMAS in the char matrix in any direction"""
    times_found = 0
    for r in range(len(soup[0])):
        for c in range(len(soup)):
            times_found += search_in_direction(soup, r, c, (1, 0))
            times_found += search_in_direction(soup, r, c, (-1, 0))
            times_found += search_in_direction(soup, r, c, (0, 1))
            times_found += search_in_direction(soup, r, c, (0, -1))
            
            times_found += search_in_direction(soup, r, c, (1, 1))
            times_found += search_in_direction(soup, r, c, (-1, 1))
            times_found += search_in_direction(soup, r, c, (1, -1))
            times_found += search_in_direction(soup, r, c, (-1, -1))
            
    return times_found

def is_x_mas_in_position(soup: list[str], row: int, column: int,) -> bool:
    """Search the X-MAC in the char matrix in a given position"""
    if row < 0 or row >= len(soup) or column < 0 or column >= len(soup[row]):
        return False
    if soup[row][column] != "A":
        return False
    
    # search M in each corner and S in the contrary (can cut execution before all checks)
    mas_found = 0
    for pos in [(( 1, -1), (-1,  1)),
                (( 1,  1), (-1, -1)),
                ((-1, -1), ( 1,  1)),
                ((-1,  1), ( 1, -1))]:
        r1 = row + pos[0][0]
        c1 = column + pos[0][1]
        r2 = row + pos[1][0]
        c2 = column + pos[1][1]
        if r1 < 0 or r1 >= len(soup) or c1 < 0 or c1 >= len(soup[row]):
            continue
        if r2 < 0 or r2 >= len(soup) or c2 < 0 or c2 >= len(soup[row]):
            continue
        if soup[r1][c1] == "M" and soup[r2][c2] == "S":
            mas_found += 1
    return mas_found == 2
    

def search_x_mas(soup: list[str]) -> int:
    """Search the X-MAS in the char matrix"""
    times_found = 0
    for r in range(len(soup[0])):
        for c in range(len(soup)):
            times_found += is_x_mas_in_position(soup, r, c)
            
    return times_found

def main() -> None:
    soup = list()
    with open("input.txt") as f:
        for line in f:
            soup.append(line.rstrip())
            
    xmas_found_times = search_xmas(soup)
    x_mas_found_times = search_x_mas(soup)
    
    print(f"XMAS Found {xmas_found_times} times")
    print(f"X-MAS Found {x_mas_found_times} times")
    
if __name__ == "__main__":
    main()