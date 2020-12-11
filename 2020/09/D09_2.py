from itertools import combinations

def format_input(inputpath):
    with open(f'{inputpath}') as f:
        lines = f.read().splitlines()

    return [int(num) for num in lines]

def get_invalid_number(input_list, preamble):

    for i in range(preamble, len(input_list)):
        to_sum = input_list[i - preamble:i]
        to_sum = list(combinations(to_sum, 2))
        for a, b in to_sum:
            if (a + b) == input_list[i]:
                break
        else:
            return input_list[i]


def min_max_sum_set(inputlist, sum_number):
    for sample_len in range(2, len(inputlist)):
        for i in range(len(inputlist)):
            try:
                numbers = input_list[i:i + sample_len]
            except IndexError:
                break
            if sum(numbers) == sum_number:
                return min(numbers) + max(numbers)




input_list = format_input('input')
invalid_number = get_invalid_number(input_list, 25)
print(invalid_number)
print(min_max_sum_set(input_list, invalid_number))