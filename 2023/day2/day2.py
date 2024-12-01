import string

def possible_game(game_info, max_red=12, max_blue=14, max_green=13) -> bool:
    print(game_info)
    for each_set in game_info:
        if each_set["red"] > max_red or each_set["blue"] > max_blue or each_set["green"] > max_green:
            return False
    return True

def game_minimums(game_info) -> (int, int, int):
    print(game_info)
    min_red = max([each_set["red"] for each_set in game_info])
    min_green = max([each_set["green"] for each_set in game_info])
    min_blue = max([each_set["blue"] for each_set in game_info])
    return min_red, min_green, min_blue

    

def main() -> None:
    possible_total = 0
    power_total = 0
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            game_id = int(line.split(":")[0].split(" ")[-1])
            print(f"Game {game_id}:")
            game_info = list()
            for each_set in line.split(":")[1].split(";"):
                game_info.append(
                    {
                        "red": 0, "blue": 0, "green": 0
                    }
                )
                for each_ball in each_set.strip().split(", "):
                    num, color = each_ball.split(" ")
                    game_info[-1][color] = int(num)

            if possible_game(game_info) is True:
                possible_total += game_id
                
            min_tuple = game_minimums(game_info)
            print(min_tuple)
            power_total += min_tuple[0] * min_tuple[1] * min_tuple[2]
                
    print(f"Possible games: {possible_total}")
    print(f"Power: {power_total}")
            

if __name__ == "__main__":
    main()