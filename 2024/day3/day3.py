import re

def parse_corrupted_code(corrupted_code:str) -> int:
    result = 0
    pairs = re.findall(r"mul\((\d{1,3},\d{1,3})\)", corrupted_code)
    for pair in pairs:
        pair = pair.split(",")
        l, r = int(pair[0]), int(pair[1])
        result += l * r
    return result

def parse_corrupted_code_enables(corrupted_code:str) -> int:
    result = 0
    enabled = True
    pairs = re.findall(r"mul\((\d{1,3},\d{1,3})\)|(d)o\(\)|do(n)'t\(\)", corrupted_code)
    for pair in pairs:
        if pair[1] == "d":
            enabled = True
        elif pair[2] == "n":
            enabled = False
        elif enabled == True:
            pair = pair[0].split(",")
            l, r = int(pair[0]), int(pair[1])
            result += l * r
    return result

def main() -> None:
    corrupted_code = ""
    with open("input.txt") as f:
        for line in f:
            corrupted_code += line
            
    total_value = parse_corrupted_code(corrupted_code)
    total_value_enables = parse_corrupted_code_enables(corrupted_code)
    print(f"Total: {total_value}")
    print(f"Total (enables): {total_value_enables}")
    
if __name__ == "__main__":
    main()