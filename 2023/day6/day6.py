import string

   

def main() -> None:
    total = 1
    times = None
    distances = None
    with open('input.txt') as f:
        for line in f:
            if line.rstrip().split(" ")[0].startswith("Time") is True:
                times = [x for x in line.rstrip().split(" ")[1:] if x != ""]
                times = ["".join(times)]
            if line.rstrip().split(" ")[0].startswith("Distance") is True:
                distances = [x for x in line.rstrip().split(" ")[1:] if x != ""]
                distances = ["".join(distances)]

    for each_race in zip(times, distances):
        each_race_wins = 0
        time = int(each_race[0])
        distance = int(each_race[1])
        print(time)
        print(distance)
        
        for p in range(time):
            e = p * (time - p)
            if e > distance:
                each_race_wins += 1
        total *= each_race_wins
    
    print(f"Total: {total}")
            

if __name__ == "__main__":
    main()
    