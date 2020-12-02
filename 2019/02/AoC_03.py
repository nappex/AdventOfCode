def addition(num_list, index_first_num, index_second_num):
    # print(num_list)
    # print(num_list[index_first_num])
    # print(num_list[index_second_num])
    return num_list[index_first_num] + num_list[index_second_num]


def multiple(num_list, index_first_num, index_second_num):
    return num_list[index_first_num] * num_list[index_second_num]


with open("02/input", mode="r") as f:
    data = f.read().strip().split(",")

data = [int(num) for num in data]
data[1] = 12
data[2] = 2

# data = [1, 1, 1, 4, 99, 5, 6, 0, 99]

for i in range(0, len(data), 4):
    opcode = data[i]
    if opcode == 1:
        data[data[i+3]] = addition(data, data[i+1], data[i+2])
    elif opcode == 2:
        data[data[i+3]] = multiple(data, data[i+1], data[i+2])
    elif opcode == 99:
        break

print(data[0])
