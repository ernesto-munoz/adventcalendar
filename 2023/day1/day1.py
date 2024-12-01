import string

number_posibilities = {"0":0,
                       "1":1, 
                       "2":2, 
                       "3":3, 
                       "4":4, 
                       "5":5, 
                       "6":6, 
                       "7":7, 
                       "8":8, 
                       "9":9,
                       "one":1,
                       "two":2,
                       "three":3, 
                       "four":4, 
                       "five":5, 
                       "six":6, 
                       "seven":7, 
                       "eight":8, 
                       "nine":9
                }
                

def search_number(line) -> str:
    earliest_number = None
    earliest_number_position = len(line) + 1
    latest_number = None
    latest_number_position = -1
    
    for each_number in number_posibilities:
        for custom_start in range(0, len(line)):
            position = line.find(each_number, custom_start)
            if -1 < position < earliest_number_position:
                earliest_number_position = position
                earliest_number = each_number
            if latest_number_position < position:
                latest_number_position = position
                latest_number = each_number
    return number_posibilities[earliest_number] * 10 + number_posibilities[latest_number]
    

def main() -> None:
    total = 0
    with open('input.txt') as f:
        for line in f:
            total += search_number(line.rstrip())
    print(total)
            

if __name__ == "__main__":
    main()
    # 54697