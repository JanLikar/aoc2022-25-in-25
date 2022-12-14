import std.stdio;
import std.algorithm;
import std.range;
import std.conv;
import std.file;
import std.string;
import std.typecons;
import std.math.algebraic;
import std.math;

alias Coordinate = Tuple!(int, "x", int, "y");

Coordinate SAND_SOURCE = Coordinate(500, 0);


bool[Coordinate] stone_line(Coordinate from, Coordinate to) {
    bool[Coordinate] stones;

    // One of dx and dy is always 0.
    auto dx = to.x - fromx;
    auto dy = to.y - from.y;

    auto distance = abs(dx + dy);

    for (auto i = 0; i < distance; i++) {
        auto x = from.x + sgn(dx) * i;
        auto y = from.y + sgn(dy) * i;
        stones[Coordinate(x, y)] = true;
    }

    return stones;
}


int load_stones(out bool[Coordinate] stones)
{
    // Returns max y.
    // bool[Coordinate] is used as a set.

    auto max_y = 0;
    auto file = File("input.txt");

    foreach (line; file.byLine()) {
        Nullable!Coordinate previous_coordinates;
        auto split = line.split(" -> ");

        foreach (point; split) {
            auto pair = strip(point).split(",");

            auto current_coordinates = tuple(to!int(pair[0]), to!int(pair[1]));

            if (current_coordinates.y > max_y) {
                max_y = current_coordinates.y;
            }

            stones[current_coordinates] = true;

            if (!previous_coordinates.isNull) {
                auto stone_line = stone_line(previous_coordinates.get, current_coordinates);
                stones = stones.byPair.chain(stone_line.byPair).assocArray;
            }
            
            previous_coordinates = current_coordinates;
        }
    }

    return max_y;
}


void main()
{
    bool[Coordinate] stones;
    auto max_y = load_stones(stones);
    auto floor_y = max_y + 2;

    bool part_1_done = false;

    // For each unit of sand:
    for (auto i = 0; i < 100000; i++) {
        auto sand_coordinates = SAND_SOURCE;

        // For each turn:
        for (auto j = 0; j < floor_y; j++) {
            if (!part_1_done && sand_coordinates[1] > max_y) {
                writeln(i);
                part_1_done = true;
            }

            if (sand_coordinates[1] + 1 == floor_y) {
                stones[sand_coordinates] = true;
                break;
            }

            // Next move
            bool blocked = true;
            auto x_directions = [0, -1, 1];
            foreach (x_direction; x_directions) {
                auto candidate = Coordinate(sand_coordinates[0] + x_direction, sand_coordinates[1] + 1);
                if (!(candidate in stones)) {
                    sand_coordinates = candidate;
                    blocked = false;
                    break;
                }
            }

            if (blocked){
                stones[sand_coordinates] = true;
                break;
            }
        }

        if (sand_coordinates == SAND_SOURCE) {
            writeln(i + 1);
            break;
        }

    }
}
