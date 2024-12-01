import string

def all_zero(sequence) -> bool:
    return all([True if x == 0 else False for x in sequence])

def get_difference_at_each_step(sequence) -> list():
    difference_sequence = list()
    for i in range(1, len(sequence)):
        difference_sequence.append(sequence[i] - sequence[i - 1])  # abs?
    return difference_sequence

def get_extrapolated_value_forward(history) -> int:
    all_difference_sequences = list()
    difference_sequence = get_difference_at_each_step(sequence=history)
    all_difference_sequences.append(difference_sequence)
    while all_zero(difference_sequence) is False:
        difference_sequence = get_difference_at_each_step(sequence=difference_sequence)
        all_difference_sequences.append(difference_sequence)

    placeholder = 0
    for each_sequence in reversed(all_difference_sequences[0:len(all_difference_sequences) - 1]):
        placeholder = placeholder + each_sequence[-1]
    
    return history[-1] + placeholder

def get_extrapolated_value_backward(history) -> int:
    all_difference_sequences = list()
    difference_sequence = get_difference_at_each_step(sequence=history)
    all_difference_sequences.append(difference_sequence)
    while all_zero(difference_sequence) is False:
        difference_sequence = get_difference_at_each_step(sequence=difference_sequence)
        all_difference_sequences.append(difference_sequence)

    placeholder = 0
    for each_sequence in reversed(all_difference_sequences[0:len(all_difference_sequences) - 1]):
        placeholder = each_sequence[0] - placeholder
    return history[0] - placeholder

def main() -> None:
    total_sum_forward = 0
    total_sum_backward = 0
    all_histories = list()
    with open('input.txt') as f:
        for line in f:
            history = [int(x) for x in line.rstrip().split(" ")]
            all_histories.append(history)
            
    for each_history in all_histories:
        total_sum_forward += get_extrapolated_value_forward(each_history)
        total_sum_backward += get_extrapolated_value_backward(each_history)
    print(f"Total sum forward: {total_sum_forward}")
    print(f"Total sum backward: {total_sum_backward}")
            

if __name__ == "__main__":
    main()
    # 54697