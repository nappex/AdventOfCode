

def trees_in_slope(x_step: int, y_step: int) -> int:
    with open('input') as f:
        slope = f.read().splitlines()

    trees = 0
    x = 0
    y = 0

    while y < len(slope):
        if slope[y][x % len(slope[y])] == '#':
            trees += 1

        x += x_step
        y += y_step

    return trees


def mul_trees_in_slopes(slopes):
    result = 1
    for x, y in slopes:
        trees = trees_in_slope(x, y)
        print('X, Y:', x, y)
        print('TREES:', trees)
        result *= trees

    return result


print(trees_in_slope(3, 1))

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
print(mul_trees_in_slopes(slopes))