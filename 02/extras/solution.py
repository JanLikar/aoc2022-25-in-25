def xyx_to_abc(move):
    mapping = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }

    return mapping[move]

def beats(a, b):
    return (
        (a == "A" and b == "C")
        or (a == "B" and b == "A")
        or (a == "C" and b == "B")
    )

def move_score(move):
    if move == "A":
        return 1
    elif move == "B":
        return 2
    else:
        return 3


def main():
    with open("input.txt") as file:
        score = 0
        for line in file:
            line = line.strip()
            # Read a space-separated string
            left, right = line.split(" ")

            right = xyx_to_abc(right)
            
            score += move_score(right)

            if left == right:
                score += 3
            elif beats(right, left):
                score += 6

    print(score)


if __name__ == "__main__":
    main()
