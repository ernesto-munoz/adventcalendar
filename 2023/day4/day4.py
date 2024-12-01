def get_points(winning, numbers) -> int:
    hits = get_matching(winning=winning, numbers=numbers)
    return 2**(hits - 1) if hits > 0 else 0

def get_matching(winning, numbers) -> int:
    hits = 0
    for each_num in numbers:
        if each_num in winning:
            hits += 1
    return hits

def main() -> None:
    points = 0
    card_copies = dict()
    with open('input.txt') as f:
        for line in f:
            card_id = int(line.rstrip().split(":")[0].split(" ")[-1])
            if card_id not in card_copies.keys():
                card_copies[card_id] = 1
            
            winning = [int (x) for x in line.rstrip().split(":")[1].split("|")[0].split(" ") if x != ""]
            numbers = [int (x) for x in line.rstrip().split(":")[1].split("|")[1].split(" ") if x != ""]
            points += get_points(winning, numbers)
            
            
            for x in range(card_copies[card_id]):
                for i in range(card_id + 1, card_id + get_matching(winning, numbers) + 1):
                    if i not in card_copies.keys():
                        card_copies[i] = 2
                    else:
                        card_copies[i] += 1
    
    print(f"Total scratchcards: {sum(card_copies.values())}")
    print(f"Points: {points}")
            

if __name__ == "__main__":
    main()