import re


def num_valid_inputs_1(inputs):
    count = 0

    for data in inputs:
        num = data['password'].count(data['symbol'])
        if data['min'] <= num <= data['max']:
            count += 1

    return count


def num_valid_inputs_2(inputs):
    count = 0

    for data in inputs:
        symbol = data['symbol']
        pos_1 = data['password'][data['min']-1]
        try:
            pos_2 = data['password'][data['max']-1]
        except IndexError:
            continue

        if (pos_1 == symbol and pos_2 != symbol):
            count += 1
        elif pos_1 != symbol and pos_2 == symbol:
            count += 1

    return count



def data_preparation(file):

    with open(file) as file:
        lines = [line.split(": ") for line in file.read().splitlines()]

    occure_regex = re.compile(r"([0-9]+)-([0-9]+) (\w{1})")

    result = []
    for policy, passw in lines:
        match = re.match(occure_regex, policy)
        if not match:
            print(f"WARNING: skipping input, ({policy}, {passw})")

        result.append(
            {
                'min': int(match.group(1)),
                'max': int(match.group(2)),
                'symbol': match.group(3),
                'password': passw,
            }
        )

    return result


data = data_preparation("input")

print(num_valid_inputs_1(data))
print(num_valid_inputs_2(data))