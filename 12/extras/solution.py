# --- Day 12: Hill Climbing Algorithm ---

import heapq
from collections import defaultdict

def height(coords, grid):
    y, x = coords
    match grid[y][x]:
        case "S":
            return ord("a")
        case "E":
            return ord("z")
        case h:
            return ord(h)


def can_move(current_height, other_height):
    return other_height - current_height <= 1


def get_available_moves(pos, grid, move_filter):
    y, x = pos
    current_height = height(pos, grid)
    max_y, max_x = len(grid) - 1, len(grid[0]) - 1 

    candidates = []

    if y > 0:
        candidates.append((y - 1, x))

    if y < max_y:
        candidates.append((y + 1, x))

    if x > 0:
        candidates.append((y, x - 1))
    
    if x  < max_x:
        candidates.append((y, x + 1))

    return [c for c in candidates if move_filter(current_height, height(c, grid))]


def filter_char(grid, char):
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == char:
                yield (i, j)

def find_end(grid):
    return next(filter_char(grid, "E"))

def find_start(grid):
    return next(filter_char(grid, "S"))


def get_distances(grid, start, move_filter=can_move):
    visited = set()
    pqueue = []
    distances = defaultdict(lambda: float("inf"))

    distances[start] = 0
    heapq.heappush(pqueue, (0, start))
    
    while len(pqueue):
        _, element = heapq.heappop(pqueue)
        visited.add(element)

        for neighbour in get_available_moves(element, grid, move_filter):
            if neighbour in visited:
                continue

            new_dist = distances[element] + 1
            if distances[neighbour] > new_dist:
                distances[neighbour] = new_dist
                heapq.heappush(pqueue, (new_dist, neighbour))


    return distances

grid = [l.strip() for l in open("input.txt").readlines()]

distances = get_distances(grid, start=find_start(grid))
part1 = distances[find_end(grid)]

distances2 = get_distances(grid, start=find_end(grid), move_filter=lambda a, b: can_move(b, a))

all_as = set(filter_char(grid, "a"))
part2 = min(distance for element, distance in distances2.items() if element in all_as)

assert part1 == 497
assert part2 == 492

print(part1)
print(part2)
