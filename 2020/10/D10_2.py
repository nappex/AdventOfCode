import pdb
from itertools import combinations

def formatted_input(inputpath):
    with open(f'{inputpath}') as f:
        return sorted([int(num) for num in f.read().splitlines()])


def main(adapters):
    count_diff = [0, 0, 0]
    source_rate = 0
    builtin_adapter = max(adapters) + 3
    adapters.append(builtin_adapter)
    adapters.insert(0, 0)
    in_row = 1
    count_in_row = []
    print(adapters)

    for adapter_joltage in adapters:
        from_adapter = [adapter_joltage - i for i in range(1, 4)]

        if source_rate in from_adapter:
            diff = adapter_joltage - source_rate
            source_rate += diff
            count_diff[diff - 1] += 1
            if diff == 1:
                print('1', adapter_joltage)
                in_row += 1
            else:
                print('else', adapter_joltage)
                count_in_row.append(in_row)
                in_row = 1

    count_in_row = list(filter(lambda x: x > 2, count_in_row))

    return count_diff, count_in_row

adapters = formatted_input('input_test_1')
differencies, diff_one = main(adapters)

print('result:')
for i, diff in enumerate(differencies, 1):
    print(f"diff {i} - {diff}x")

print(differencies[0] * differencies[2])
print(diff_one)
result = 1
for count_diff in diff_one:
    num_count = count_diff - 2
    result *=  num_count ** 2
print(result)




