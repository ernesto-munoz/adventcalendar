from pprint import pprint

def get_disk_expanded(disk_map: str) -> list:
    disk_expanded = list()
    file = True
    file_id = 0
    for c in disk_map:
        if file is True:  # as a file
            for i in range(int(c)):
                disk_expanded.append(str(file_id))
            file_id += 1
        else:  # as free space
            for i in range(int(c)):
                disk_expanded.append(".")
        file = not file
    return disk_expanded

def move_disk(disk_expanded:list) -> list:
    L, R = 0, len(disk_expanded) - 1
    while L != R:
        if disk_expanded[L] != ".":
            L += 1
        if disk_expanded[R] == ".":
            R -= 1
        if disk_expanded[L] == "." and disk_expanded[R] != ".":
            disk_expanded[L], disk_expanded[R] = disk_expanded[R], disk_expanded[L]
            L += 1
            R -= 1

    return disk_expanded

def move_disk2(disk_expanded:str) -> list:
    free_disk_index = 0
    
    return disk_expanded
            
def get_checksum(disk_expanded:list) -> int:
    checksum = 0
    for i in range(0, len(disk_expanded)):
        if disk_expanded[i] == ".":
            continue
        checksum += i * int(disk_expanded[i])
    return checksum

def main() -> None:
    
    disk_map:str = None
    with open("test.txt") as f:
        for line in f:
            disk_map = line.rstrip()
    print(f"The disk map is: {disk_map}")
    disk_expanded = get_disk_expanded(disk_map)
    print(f"The disk map extended is: {disk_expanded}")
    
    # disk_expanded_defrag = move_disk(list(disk_expanded))
    # print(f"The disk map extended and defrag is: {disk_expanded_defrag}")
    # print(f"The checksum is: {get_checksum(disk_expanded_defrag)}")
    
    disk_expanded_defrag = move_disk2(list(disk_expanded))
    print(f"The disk map extended and defrag is (second method): {disk_expanded_defrag}")
    print(f"The checksum is: {get_checksum(disk_expanded_defrag)}")

    
    
if __name__ == "__main__":
    main()