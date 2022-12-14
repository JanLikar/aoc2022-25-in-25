import dataclasses

@dataclasses.dataclass(eq=True, frozen=True)
class Coordinate():
    x: int
    y: int       

    def __add__(self, other):
        if isinstance(other, tuple):
            x = other[0]
            y = other[1]
        else:
            x = other.x
            y = other.y

        return Coordinate(self.x + x, self.y + y)

SAND_SOURCE = Coordinate(500, 0)


def read_stone():
    stone = set()
    with open("input.txt") as f:
        for line in f.readlines():
            prev_coordinate = None
            for point in line.split("->"):
                point = point.strip()
                x, y = point.split(",")
                coordinate = Coordinate(int(x), int(y))

                stone.add(coordinate)

                if prev_coordinate is not None:
                    stone.update(get_stone_line(prev_coordinate, coordinate))

                prev_coordinate = coordinate

        return stone


def get_stone_line(prev_coordinate, coordinate):
    if prev_coordinate.x == coordinate.x:
        # moves across y
        line_lenght = abs(prev_coordinate.y - coordinate.y)
        coordinate_change = (0, 1) if coordinate.y > prev_coordinate.y else (0, -1)
    elif prev_coordinate.y == coordinate.y:
        line_lenght = abs(prev_coordinate.x - coordinate.x)
        coordinate_change = (1, 0) if coordinate.x > prev_coordinate.x else (-1, 0)
    else:
        raise ValueError("Stone coordinates not in line")

    for i in range(line_lenght):
        prev_coordinate +=coordinate_change
        yield prev_coordinate


STONE = read_stone()
MAX_STONE_Y = max(s.y for s in STONE)
FLOOR_Y = MAX_STONE_Y + 2

# Simulation loop

for i in range(100000):
    grain_coordinates = SAND_SOURCE

    for j in range(100000):

        #print(grain_coordinates.y, MAX_STONE_Y)
        if grain_coordinates.y > MAX_STONE_Y:
            # Goes to infinity, simulation done
            print(f"Part1 done, n_blocked = {i}")

        if grain_coordinates.y + 1 == FLOOR_Y:
            print("Floor")
            STONE.add(grain_coordinates)
            break

        move_directions = ((0, 1), (-1, 1), (1, 1))
        for move in move_directions:
            if grain_coordinates + move not in STONE:
                grain_coordinates += move
                break
        else:
            STONE.add(grain_coordinates)
            break
        
    if grain_coordinates == SAND_SOURCE:
        print(f"Part2 done, n_blocked = {i + 1}")
        break

