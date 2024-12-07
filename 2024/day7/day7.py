from pprint import pprint

def get_operator_combinations(length:int, operators=list) -> list:
    """Get all possible combinations for the operators with a given lenght"""
    if(length == 1):
        return [[_] for _ in operators]
    
    result = get_operator_combinations(length - 1, operators)
    final_result = list()
    for r in result:
        for op in operators:
            final_result.append([op] + r)
        
    return final_result
    
def is_possible_operation(numbers:list[int], result:int, operators=list[callable]) -> bool:
    """Check if any combination of the operators can bring the result from the list of numbers"""
    operators_list = get_operator_combinations(len(numbers) - 1, operators=operators)
    
    for operators in operators_list:
        previous_operation_result = numbers[0]
        for i in range(1,len(numbers)):
            previous_operation_result = operators[i - 1](previous_operation_result, numbers[i])
        
        if previous_operation_result == result:
            return True
    
    return False
    
def main() -> None:
    
    total_first = 0
    total_second = 0
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip().split(":")
            result = int(line[0])
            operation_numbers = [int(n) for n in line[1].strip().split(" ")]
            operators_first = [lambda x, y: x + y, lambda x, y: x * y]
            if is_possible_operation(operation_numbers, result, operators_first) is True:
                total_first += result
                
            operators_second = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: x * 10 ** len(str(y)) + y]
            if is_possible_operation(operation_numbers, result, operators_second) is True:
                total_second += result
                 

    print(f"The total result of the possible operations is {total_first}")
    print(f"The total result of the possible operations (with concant) is {total_second}")

    
            


    
if __name__ == "__main__":
    main()