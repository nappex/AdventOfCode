from copy import deepcopy


def formatted_input(inputpath):
    with open(f'{inputpath}') as f:
        return [list(line) for line in f.read().splitlines()]


def count_onview(hall, pos_y, pos_x):
    # values how is change the pos_y and pos_x
    # to check all positions around specific point
    max_len = sorted([len(hall), len(hall[0])], reverse=True)[0]
    changes = (-1, 0, 1)
    occupied_seats = 0
    for y in changes:
        for x in changes:
            for n in range(1, max_len):
                if y == 0 and x == 0:
                    continue
                y_to_check = pos_y + (y * n)
                x_to_check = pos_x + (x * n)
                if y_to_check < 0 or x_to_check < 0:
                    continue
                try:
                    if hall[y_to_check][x_to_check] == '#':
                        occupied_seats += 1
                        break
                    elif hall[y_to_check][x_to_check] == 'L':
                        break
                except IndexError:
                    continue

    return occupied_seats


def are_halls_same(a, b):
    rows, cols = len(a), len(a[0])
    for y in range(rows):
        for x in range(cols):
            if a[y][x] != b [y][x]:
                return False

    return True

def print_hall(hall):
    for row in hall:
        print("".join(row))

    print('-'*30)

def get_stable_hall(hall):
    empty_seat = 'L'
    occupied_seat = '#'
    floor = '.'
    y_max, x_max = len(hall), len(hall[0])
    previous_hall = hall
    current_hall = deepcopy(hall)

    while True:
        for y in range(y_max):
            for x in range(x_max):
                symbol = previous_hall[y][x]
                if symbol == floor:
                    current_hall[y][x] = floor
                    continue

                num_occupied = count_onview(previous_hall, y, x)
                if symbol == empty_seat and num_occupied == 0:
                    current_hall[y][x] = occupied_seat
                elif symbol == occupied_seat and num_occupied > 4:
                    current_hall[y][x] = empty_seat

        if are_halls_same(previous_hall, current_hall):
            return current_hall

        previous_hall = deepcopy(current_hall)

def count_occupied_seat(hall):
    occupied = 0
    rows, cols = len(hall), len(hall[0])
    for y in range(rows):
        for x in range(cols):
            if hall[y][x] == '#':
                occupied += 1

    return occupied

hall = formatted_input('input')
stable_hall = get_stable_hall(hall)

print(count_occupied_seat(stable_hall))


