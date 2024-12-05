
def is_correct_update(update:list[int], rules:dict) -> bool:
    """Check if the update is correct with the given rules N2"""
    for i in range(0, len(update)):
        for j in range(i + 1, len(update)):
            if update[i] in rules.keys() and update[j] in rules[update[i]]:
                return False
    return True

def get_middle_number(update:list[int]) -> int:
    """Get the middle number of a list"""
    index = int(len(update) / 2)
    return update[index]

def get_correct_update(update:list[int], rules:dict) -> list[int]:
    """Correct an update swapping the elements that are in incorrect order N2 (may be another more efficient way to do it?)"""
    corrected_update = update.copy()
    for i in range(0, len(corrected_update)):
        for j in range(i + 1, len(corrected_update)):
            if corrected_update[i] in rules.keys() and corrected_update[j] in rules[corrected_update[i]]:
                corrected_update[i], corrected_update[j] = corrected_update[j], corrected_update[i]
    return corrected_update

def main() -> None:
    rules = dict()
    updates = list()
    reading_rules: bool = True
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip()
            if line == "":
                reading_rules = False
                continue
            if reading_rules:
                rule = line.split("|")
                before, after = int(rule[0]), int(rule[1])
                if after in rules.keys():
                    rules[after].append(before)
                else:
                    rules[after] = [before]
            else:
                updates.append([int(n) for n in line.split(",")])

    # first part of the puzzle
    total_correct_updates_middle_number: int = 0
    for update in updates:
        is_correct = is_correct_update(update, rules)
        number = get_middle_number(update)
        # print(f"Update {update} is {is_correct} with middle number {number}")
        if is_correct is True:
            total_correct_updates_middle_number += number
    print(f"The total middle number of the correct updates is {total_correct_updates_middle_number}")
    
    # second part of the puzzle
    total_corrected_updates_middle_number: int = 0
    for update in updates:
        is_correct = is_correct_update(update, rules)
        if is_correct is False:
            corrected_update = get_correct_update(update, rules)
            number = get_middle_number(corrected_update)
            # print(f"Update {update} is now corrected as {corrected_update} with middle number {number}")
            total_corrected_updates_middle_number += number
    print(f"The total middle number of the corrected updates is {total_corrected_updates_middle_number}")
    
if __name__ == "__main__":
    main()