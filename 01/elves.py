def lines_to_elves(lines):
    snacks = []
    for line in lines:
        stripped_line = line.strip()

        if stripped_line == "":
            yield snacks
            snacks = []
        else:
            snacks.append(int(stripped_line))
 

def sum_top_3(elves):
    return sum(sorted(elves)[-3:])


if __name__ == "__main__":
    with open("elves.txt") as file:
        elves = lines_to_elves(file)
        total_snacks_per_elf = list(map(sum, elves))

    print(max(total_snacks_per_elf))
    print(sum_top_3(total_snacks_per_elf))
