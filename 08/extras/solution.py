import math


def get_view_slices(grid, tree_x, tree_y):
    row = grid[tree_y]
    col = [n[tree_x] for n in grid]

    return [
        row[0:tree_x][::-1],
        row[tree_x+1:],
        col[0:tree_y][::-1],
        col[tree_y + 1:],
    ]


def dist_to_first(view, tree_height):
    return next(
        (dist + 1 for dist, height in enumerate(view) if height >= tree_height),
        len(view),
    )


def sees_edge(view, tree_height):
    return all(v < tree_height for v in view)


input = open("input.txt").read()
rows = [list(row) for row in input.splitlines()]


scores = []
visible_count = 0

for y, rows in enumerate(input):
    for x, tree_height in enumerate(rows):
        slices = get_view_slices(input, x, y)
        dists = [dist_to_first(s, tree_height) for s in slices]

        scores.append(math.prod(dists))

        if any(sees_edge(s, tree_height) for s in slices):
            visible_count += 1

print(visible_count)
print(max(scores))
