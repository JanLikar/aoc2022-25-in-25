def move(pos, direction):
    match direction:
        case "R":
            return (pos[0] + 1, pos[1])
        case "L":
            return (pos[0] - 1, pos[1])
        case "U":
            return (pos[0], pos[1] + 1)
        case "D":
            return (pos[0], pos[1] - 1)
    

def tail_move(tail, head):
    tail_x, tail_y = tail
    head_x, head_y = head
    new_tail = tail

    should_move = abs(tail_x - head_x) > 1 or abs(tail_y - head_y) > 1

    if not should_move:
        return tail

    if head_x > tail_x:
        new_tail = move(new_tail, "R")
    elif head_x < tail_x:
        new_tail = move(new_tail, "L")

    if head_y > tail_y:
        new_tail = move(new_tail, "U")
    elif head_y < tail_y:
        new_tail = move(new_tail, "D")

    return new_tail
    

def count_visited_squares(moves, tail_len=1):
    start = (0, 0)
    visited = set()

    head = start
    tail = [start] * tail_len

    for (direction, count) in moves:
        for _ in range(int(count)):
            head = move(head, direction)

            neighbour = head
            for i, t in enumerate(tail):
                tail[i] = tail_move(t, neighbour)
                neighbour = tail[i]

            visited.add(tail[-1])

    return len(visited)


moves = [m.split() for m in open("input.txt").readlines()]

print(count_visited_squares(moves))
print(count_visited_squares(moves, 9))
