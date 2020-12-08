text_test = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""
with open('input') as f:
     INSTRUCTIONS = f.read().strip().splitlines()
# INSTRUCTIONS = text_test.strip().splitlines()


def get_instruction(index):
    return INSTRUCTIONS[index].split(' ')


def main():

    accumulate = 0
    position = 0
    visited = []

    while position not in visited:
        command, value = get_instruction(position)
        visited.append(position)

        if command == 'acc':
            accumulate += int(value)
            position += 1
        elif command == 'jmp':
            position += int(value)
        else:
            position += 1

    return accumulate


print(main())

