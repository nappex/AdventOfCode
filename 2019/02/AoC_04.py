def addition(num_list, index_first_num, index_second_num):
    # print(num_list)
    # print(num_list[index_first_num])
    # print(num_list[index_second_num])
    return num_list[index_first_num] + num_list[index_second_num]


def multiple(num_list, index_first_num, index_second_num):
    return num_list[index_first_num] * num_list[index_second_num]


def infinite_sequence():
    for i in range(100):
        for j in range(100):
            yield i, j


gen = infinite_sequence()


with open("02/input", mode="r") as f:
    data = f.read().strip().split(",")

data = [int(num) for num in data]
r_data = [1]
while r_data[0] != 19690720:
    r_data = list(data)
    r_data[1], r_data[2] = next(gen)

    for i in range(0, len(data), 4):
        opcode = r_data[i]
        if opcode == 1:
            try:
                r_data[r_data[i+3]
                       ] = addition(r_data, r_data[i+1], r_data[i+2])
            except IndexError:
                break
        elif opcode == 2:
            try:
                r_data[r_data[i+3]
                       ] = multiple(r_data, r_data[i+1], r_data[i+2])
            except IndexError:
                break
        elif opcode == 99:
            break


print(r_data)
print()
print(f"result: {r_data[1]*100 + r_data[2]}")
