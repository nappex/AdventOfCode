import sys

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


def format_input(input_string):
    lines = input_string.splitlines()

    original_instructions = []
    for line in lines:
        command, value = line.split()
        original_instructions.append((command, int(value)))

    return original_instructions



def main(instructions):
    accumulate = 0
    index = 0
    visited = []

    while index not in visited:
        try:
            command, value = instructions[index]
        except IndexError:
            if index < 0:
                return 'mensi index nez 0'
            else:
                return 'vetsi index nez 0'

        visited.append(index)

        if command == 'acc':
            accumulate += value
            index += 1
        elif command == 'jmp':
            index += value
        elif command == 'nop':
            index += 1
        else:
            raise RuntimeError("I cannot resolve this command")

    return accumulate


with open('input') as f:
     input_string = f.read()

original_instructions = format_input(input_string)
print(main(original_instructions))

