from pprint import pprint
from functools import lru_cache, cache

@cache
def get_num_digits(n:int) -> int:
    """Get the number of digits used to represent an integer number"""
    digits: int = 0
    while n:
        n //= 10
        digits += 1
    return digits

@cache
def get_splitted_number(n:int, num_digits:int) -> tuple[int]:
    denominator = 10 ** (num_digits // 2)
    r = n % (10 ** (num_digits // 2))
    # print(n, num_digits, (n - r) // denominator, r)
    return ((n - r) // denominator, r)

@cache
def transform(n:int) -> list[int]:
    if n == 0:  # rule 1: if the number is 0, it's replaced by 1
        return [1]
    
    if (num_digits := get_num_digits(n)) % 2 == 0:  # rule 2: if the number of digits is even; split
        l, r = get_splitted_number(n, num_digits)
        return [l, r]

    return [n * 2024]

# @cache
def blink(stones:list[int]) -> list[int]:
    new_stones = list()
    for i in range(len(stones)):
        new_stones.extend(transform(stones[i]))
        # if stones[i] == 0:  # rule 1: if the number is 0, it's replaced by 1
        #     new_stones.append(1)
        # elif (num_digits := get_num_digits(stones[i])) % 2 == 0:  # rule 2: if the number of digits is even; split
        #     l, r = get_splitted_number(stones[i], num_digits)
        #     new_stones.append(l)
        #     new_stones.append(r)
        # else:
        #     new_stones.append(stones[i] * 2024)

    return new_stones

def main() -> None:    
    stones = list()
    with open("input.txt") as f:
        for line in f:
            stones = [int(_) for _ in line.rstrip().split(" ")]


    print(f"Original: {stones}")
    for i in range(75):
        stones = blink(stones)
        print(f"Blink {i + 1}: {1}")
    print(f"Total stones: {len(stones)}")
    
    

    
    
if __name__ == "__main__":
    main()