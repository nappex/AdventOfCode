from itertools import product

def binary_tree(a, b, low_symbol, up_symbol):
    rows = list(range(a, b))
    index = len(rows) // 2
    if index  == 1:
        low_range = (rows[0],)
        up_range = (rows[1],)
    else:
        median = rows[index]
        low_range = (a, median)
        up_range = (median, b)

    return {low_symbol: low_range, up_symbol: up_range}


def get_row_number(code, start_node=(0, 128)):
    code = code.upper()
    a, b = start_node
    for symbol in code:
        low_up = binary_tree(a, b, 'F', 'B')
        if len(low_up[symbol]) > 1:
            a, b = low_up[symbol]
        else:
            return low_up[symbol][0]


def get_column_number(code, start_node=(0, 8)):
    code = code.upper()
    a, b = start_node
    for symbol in code:
        low_up = binary_tree(a, b, 'L', 'R')
        if len(low_up[symbol]) > 1:
            a, b = low_up[symbol]
        else:
            return low_up[symbol][0]


def get_seatID(code):
    row_code, column_code = code[:7], code[7:]
    row = get_row_number(row_code)
    column = get_column_number(column_code)
    return (row, column)

with open('input') as f:
    batch = f.read().splitlines()
    all_seats_found = set(get_seatID(code) for code in batch)
    min_row = min(all_seats_found, key=lambda a: a[0])[0]
    max_row = max(all_seats_found, key=lambda a: a[0])[0]
    min_col = min(all_seats_found, key=lambda a: a[1])[1]
    max_col = max(all_seats_found, key=lambda a: a[1])[1]
    all_seats = set(
        product(
            range(min_row, max_row + 1),
            range(min_col, max_col + 1),
            )
        )

    missing_seats = all_seats.difference(all_seats_found)
    for seat in missing_seats:
        if min_row < seat[0] < max_row:
            print(seat, seat[0] * 8 + seat[1])
