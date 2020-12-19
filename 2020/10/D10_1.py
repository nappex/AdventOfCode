def formatted_input(inputpath):
    with open(f'{inputpath}') as f:
        return sorted([int(num) for num in f.read().splitlines()])


def main(adapters):
    count_diff = [0, 0, 0]
    source_rate = 0
    builtin_adapter = max(adapters) + 3
    adapters.append(builtin_adapter)

    for adapter_joltage in adapters:
        from_adapter = [adapter_joltage - i for i in range(4)]

        if source_rate in from_adapter:
            diff = adapter_joltage - source_rate
            source_rate += diff
            count_diff[diff - 1] += 1

    return count_diff

adapters = formatted_input('input')
result = main(adapters)

print('result:')
for i, diff in enumerate(result, 1):
    print(f"diff {i} - {diff}x")

print(result[0] * result[2])





