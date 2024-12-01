
import functools

# card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def _get_letters_info(hand:str) -> dict:
    letters = dict()
    for h in hand:
        if h not in letters:
            letters[h] = 0
        letters[h] += 1
    return letters

def _get_hands_with_wildcard(hand:str) -> list:
    hands = [hand]
    for c in card_order[1:]:
        if "J" in hand:
            hands.append(hand.replace("J", c))
    return hands

def is_five_of_a_kind(hand:str) -> bool:
    all_hands = _get_hands_with_wildcard(hand)
    for each_hand in all_hands:
        letters = _get_letters_info(hand=each_hand)
        if list(letters.values()) == [5]:
            return True
    return False

def is_four_of_a_kind(hand:str) -> bool:
    all_hands = _get_hands_with_wildcard(hand)
    for each_hand in all_hands:
        letters = _get_letters_info(hand=each_hand)
        if sorted(list(letters.values())) == [1, 4]:
            return True
    return False

def is_full_house(hand:str) -> bool:
    all_hands = _get_hands_with_wildcard(hand)
    for each_hand in all_hands:
        letters = _get_letters_info(hand=each_hand)
        if sorted(list(letters.values())) == [2, 3]:
            return True
    return False

def is_three_of_a_kind(hand:str) -> bool:
    all_hands = _get_hands_with_wildcard(hand)
    for each_hand in all_hands:
        letters = _get_letters_info(hand=each_hand)
        if sorted(list(letters.values())) == [1, 1, 3]:
            return True
    return False

def is_two_pair(hand:str) -> bool:
    all_hands = _get_hands_with_wildcard(hand)
    for each_hand in all_hands:
        letters = _get_letters_info(hand=each_hand)
        if sorted(list(letters.values())) == [1, 2, 2]:
            return True
    return False

def is_one_pair(hand:str) -> bool:
    all_hands = _get_hands_with_wildcard(hand)
    for each_hand in all_hands:
        letters = _get_letters_info(hand=each_hand)
        if sorted(list(letters.values())) == [1, 1, 1, 2]:
            return True
    return False

def get_hand_value(hand:str) -> int:
    if is_five_of_a_kind(hand) is True:
        return 7
    elif is_four_of_a_kind(hand) is True:
        return 6
    elif is_full_house(hand) is True:
        return 5
    elif is_three_of_a_kind(hand) is True:
        return 4
    elif is_two_pair(hand) is True:
        return 3
    elif is_one_pair(hand) is True:
        return 2
    return 1

def compare(left, right) -> int:
    lv = get_hand_value(left[0])
    rv = get_hand_value(right[0])
    if lv > rv:
        return 1
    elif lv < rv:
        return -1
    
    for i, _ in enumerate(left[0]):
        if card_order.index(left[0][i]) > card_order.index(right[0][i]):
            return 1
        elif card_order.index(left[0][i]) < card_order.index(right[0][i]):
            return -1
    return 0

def main() -> None:

    hands = list()
    with open('input.txt') as f:
        for line in f:
            hands.append((line.rstrip().split(" ")[0], int(line.rstrip().split(" ")[1])))
            
    print(hands)
    hands.sort(key=functools.cmp_to_key(compare))
    print(hands)
    total = sum([hands[i][1] * (i + 1) for i in range(len(hands))])
    print(f"Total: {total}")
            

if __name__ == "__main__":
    main()
    