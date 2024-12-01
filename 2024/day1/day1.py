import string

def find_distance(left:list[int], right:list[int]) -> int:
    left.sort()
    right.sort()

    distance = 0    
    for i, _ in enumerate(left):
        l, r = left[i], right[i]
        distance += abs(l - r)
    
    return distance

def find_similarity(left:list[int], right:list[int]) -> int:
    similarity = 0
    for i, number in enumerate(left):
        num_times = right.count(number)
        print(number, num_times)
        similarity += number * num_times
        
    return similarity

def main() -> None:
    left, right = list(), list()
    with open('input.txt') as f:
        for line in f:
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))
    print("Distance: {}".format(find_distance(left, right)))
    print("Similarity: {}".format(find_similarity(left, right)))
            

if __name__ == "__main__":
    main()