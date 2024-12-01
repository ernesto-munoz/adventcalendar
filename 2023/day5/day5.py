import string
from collections.abc import Sequence

maps_order = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]   

def get_lowest_location(seeds_range:Sequence, mappers:dict) -> int:
    lowest = float("inf")
    # lowest location
    for seed in seeds_range:
        location = seed
        for map in maps_order:
            for each_mapping in mappers[map]:
                if location in each_mapping["origin"]:
                    location = each_mapping["destiny"][each_mapping["origin"].index(location)]
                    break
        if location < lowest:
            lowest = location
    return lowest
    

def main() -> None:
    seeds = None
    mappers = dict()
    
    print("Parsing input...")
    with open('input.txt') as f:
        active_mapper = None
        for line in f:
            if line.rstrip().startswith("seeds:") is True:
                seeds = line.rstrip().split(" ")[1:]
                seeds = [int(seed) for seed in seeds]
            else:
                splitted_line = line.rstrip().split(" ")
                match len(splitted_line):
                    case 2:
                        active_mapper = splitted_line[0]
                    case 3:
                        if active_mapper not in mappers:
                            mappers[active_mapper] = list()
                        
                        dest = int(splitted_line[0])    
                        org = int(splitted_line[1])
                        l = int(splitted_line[2])

                        mappers[active_mapper].append({
                            "origin": range(org, org + l),
                            "destiny": range(dest, dest + l)
                        })
                    case other:
                        pass
        
    print(f"Seeds: {seeds}")
    from pprint import pprint
    pprint(mappers)
    
    # seeds to range seeds
    seeds_range = list()
    for seed in zip(seeds[::2], seeds[1::2]):
        seeds_range.append(range(seed[0], seed[0] + seed[1]))
    
    lowest_location = float("inf")
    for each_seed_range in seeds_range:
        print(each_seed_range)
        lowest = get_lowest_location(seeds_range=each_seed_range, mappers=mappers)
        if lowest < lowest_location:
            lowest_location = lowest
                
    print(f"Lowest location: {lowest_location}")
            

if __name__ == "__main__":
    main()