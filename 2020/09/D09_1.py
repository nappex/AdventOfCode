def format_input(inputpath):
    with open(f'{inputpath}') as f:
        lines = f.read().splitlines()

    return [int(num) for num in lines]

def main(input_list, preamble):

    for i in range(preamble, len(input_list)):
        to_sum = input_list[i - preamble:i]
        to_sum = list(combinations(to_sum, 2))
        for a, b in to_sum:
            if (a + b) == input_list[i]:
                break
        else:
            return input_list[i]



input_list = format_input('input')
print(main(input_list, 25))