def create_wire(wire_directions):
    directions = {"R": (1, 0),
                  "U": (0, 1),
                  "L": (-1, 0),
                  "D": (0, -1)}

    wire = [[0, 0]]

    for move in wire_directions:
        x_direct, y_direct = directions[move[0]]
        x_direct, y_direct = x_direct * move[1], y_direct * move[1]
        x_move, y_move = wire[-1]
        wire.append([x_move + x_direct, y_move + y_direct])

    return wire


def multiple_vectors(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]


def get_cross_points(wire_1, wire_2):
    cross_points = []
    for i, coor1 in enumerate(wire_1):
        for j, coor2 in enumerate(wire_2):
            try:
                A1, B1 = coor1, wire_1[i+1]
                A2, B2 = coor2, wire_2[j+1]
            except IndexError:
                continue
            d_vector1 = [B1[0] - A1[0], B1[1] - A1[1]]
            d_vector2 = [B2[0] - A2[0], B2[1] - A2[1]]

            if multiple_vectors(d_vector1, d_vector2) == 0:
                if A1[0] == B1[0] and A2[1] == B2[1]:
                    if min(A1[1], B1[1]) <= A2[1] <= max(A1[1], B1[1]) \
                            and min(A2[0], B2[0]) <= A1[0] <= max(A2[0], B2[0]):
                        cross_points.append([A1[0], A2[1]])
                elif A1[1] == B1[1] and A2[0] == B2[0]:
                    if min(A1[0], B1[0]) <= A2[0] <= max(A1[0], B1[0]) \
                            and min(A2[1], B2[1]) <= A1[1] <= max(A2[1], B2[1]):
                        cross_points.append([A2[0], A1[1]])

    try:
        cross_points.remove([0, 0])
    except ValueError:
        pass

    return cross_points


def wire_allpoints(moves):
    directions = {"R": (1, 0),
                  "U": (0, 1),
                  "L": (-1, 0),
                  "D": (0, -1)}
    wire = [(0, 0)]
    for move in moves:
        mx, my = directions[move[0]]
        for _ in range(move[1]):
            wx, wy = wire[-1]
            wire.append((mx + wx, my + wy))
    del wire[0]

    return wire


def count_steps(wire1, wire2, cross_points):
    result = []
    for coor in cross_points:
        result.append(wire1.index(coor) + wire2.index(coor) + 2)
    # temp = []
    # for cross in cross_points:
    #     for n, point in enumerate(wire, 1):
    #         if point == cross:
    #             result.append(n)

    return min(result)


def convert_code(coor_list):
    return [(coor[0], int(coor[1:])) for coor in coor_list]


def main():
    with open("03/input", mode="r") as f:
        data = [line.strip().split(",") for line in f]

    wire_1, wire_2 = data
    wire_1_lines = create_wire(convert_code(wire_1))
    wire_2_lines = create_wire(convert_code(wire_2))
    wire_1_allpoints = wire_allpoints(convert_code(wire_1))
    wire_2_allpoints = wire_allpoints(convert_code(wire_2))
    cross_points_2 = set(wire_1_allpoints).intersection(set(wire_2_allpoints))
    cross_points = get_cross_points(wire_1_lines, wire_2_lines)
    print(len(cross_points_2))
    print(len(cross_points))

    # wire1_steps = min(count_steps(wire_1_allpoints, cross_points_2))

    # wire2_steps = min(count_steps(wire_2_allpoints, cross_points_2))
    steps = count_steps(wire_1_allpoints, wire_2_allpoints, cross_points_2)
    closest_point = min([abs(a) + abs(b) for a, b in cross_points])
    closest_point_2 = min([abs(a) + abs(b) for a, b in cross_points_2])
    print(f"Distance: {closest_point, closest_point_2}")
    print(f"Steps: {steps}")


if __name__ == "__main__":
    main()
